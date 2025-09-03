# app.py
import os
import logging
from threading import Thread
import asyncio
from flask import Flask, request
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
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
global ptb_application
flask_app = Flask(__name__)

ptb_application = None

def run_ptb_in_thread(app: Application, loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(app.initialize())
    loop.run_until_complete(app.start())
    loop.run_until_complete(app.updater.start_polling())
    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(app.updater.stop())
        loop.run_until_complete(app.stop())



def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("reply", reply_command))
    app.add_handler(MessageHandler(filters.Regex("^📲 إظهار القائمة$"), handle_reply_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

@flask_app.route(f"/webhook/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), ptb_application.bot)
    asyncio.run_coroutine_threadsafe(
        ptb_application.process_update(update),
        ptb_application.bot.loop
    )
    return "OK", 200

@flask_app.route("/")
def index():
    return "TENTH POWER BOT is Running!", 200

if __name__ == "__main__":
   
    ptb_app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    setup_handlers(ptb_app)
 
    ptb_application = ptb_app

    ptb_event_loop = asyncio.new_event_loop()
    ptb_thread = Thread(target=run_ptb_in_thread, args=(ptb_app, ptb_event_loop), name="PTBThread")
    ptb_thread.daemon = True
    ptb_thread.start()
    logger.info("PTB thread started.")

    if os.getenv("WEBHOOK_URL"):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(ptb_app.bot.set_webhook(url=f"{os.getenv('WEBHOOK_URL')}/webhook/{os.getenv('TELEGRAM_TOKEN')}"))
        loop.close()
        logger.info(f"Webhook set to {os.getenv('WEBHOOK_URL')}/webhook/{os.getenv('TELEGRAM_TOKEN')}")

        port = int(os.environ.get("PORT", 10000))
        logger.info(f"Starting Flask app on port {port}")
        flask_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
    else:
        logger.info("No WEBHOOK_URL set. Running in polling mode.")
        asyncio.run(ptb_app.run_polling())

    if ptb_event_loop.is_running():
        ptb_event_loop.call_soon_threadsafe(ptb_event_loop.stop)
    ptb_thread.join()
    logger.info("Application shutdown complete.")