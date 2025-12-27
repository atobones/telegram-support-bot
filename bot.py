import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from config import BOT_TOKEN, ADMIN_ID, DB_PATH
from db import init_db, log_message, get_stats

WELCOME_TEXT = (
    "Hello! 👋\n"
    "Send a message and I will log it.\n"
    "This is a minimal support/leads bot template."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_TEXT)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if ADMIN_ID and update.effective_user and update.effective_user.id != ADMIN_ID:
        return

    total, users = get_stats(DB_PATH)
    await update.message.reply_text(f"📊 Stats\nMessages: {total}\nUsers: {users}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    msg = update.message

    if not user or not msg:
        return

    username = user.username or ""
    full_name = (user.full_name or "").strip()
    text = msg.text or ""

    log_message(DB_PATH, user.id, username, full_name, text)
    await msg.reply_text("✅ Received. Thanks!")

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Set it via environment variable BOT_TOKEN.")

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    init_db(DB_PATH)

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.run_polling()

if __name__ == "__main__":
    main()
