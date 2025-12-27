# Telegram Support Bot (Python)

Minimal and extensible template for a business Telegram bot:
support and lead collection with structured data storage.

## Core features
- /start onboarding
- Message logging to SQLite
- Save user uploads into folders by user_id
- Basic admin statistics

## Can be extended with
- Task assignment between managers
- SLA alerts for unanswered messages
- Broadcast messages to all users
- User/Request unique ID system
- CRM or Google Sheets integration

## Environment
- Create `.env`:
- BOT_TOKEN=your_token_here
- ADMIN_ID=123456789
- DB_PATH=data/app.db

## Tech stack
- Python
- python-telegram-bot
- SQLite

## Use cases
- Customer support bot
- Lead capture bot
- Internal request workflow
- Small business automation

## Setup (quick)
1. Create a bot via @BotFather
2. Add `BOT_TOKEN` to `.env` (or config)
3. Install deps: `pip install -r requirem
4. pip install -r requirements.txt
5. export BOT_TOKEN="..."
6. python bot.py

