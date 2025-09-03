import os
import logging
import asyncio
from quart import Quart, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    Application
)
from handlers import start, button_handler, message_handler, reply_command, handle_reply_buttons
from config import TELEGRAM_TOKEN, WEBHOOK_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

quart_app = Quart(__name__)
ptb_app: Application = None  # البوت

# ======== إعداد Handlers ========
def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("reply", reply_command))
    app.add_handler(MessageHandler(filters.Regex("^📲 إظهار القائمة$"), handle_reply_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))


# ======== Webhook endpoint ========
@quart_app.route(f"/webhook/{TELEGRAM_TOKEN}", methods=["POST"])
async def webhook():
    data = await request.get_json()
    update = Update.de_json(data, ptb_app.bot)
    await ptb_app.process_update(update)
    return "OK", 200


@quart_app.route("/")
async def index():
    return "TENTH POWER BOT is Running!", 200


# ======== Main ========
async def main():
    global ptb_app
    ptb_app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    setup_handlers(ptb_app)

    await ptb_app.initialize()
    await ptb_app.start()

    if WEBHOOK_URL:
        await ptb_app.bot.set_webhook(url=f"{WEBHOOK_URL}/webhook/{TELEGRAM_TOKEN}")
        logger.info(f"Webhook set to {WEBHOOK_URL}/webhook/{TELEGRAM_TOKEN}")
        port = int(os.environ.get("PORT", 10000))
        logger.info(f"Starting Quart app on port {port}")
        await quart_app.run_task(host="0.0.0.0", port=port)
    else:
        logger.info("No WEBHOOK_URL set. Running in polling mode.")
        await ptb_app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
