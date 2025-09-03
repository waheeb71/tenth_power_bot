# app.py
import os
import logging
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
from config import TELEGRAM_TOKEN, WEBHOOK_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

flask_app = Flask(__name__)
ptb_app: Application = None  # نوع البوت

# ======== إعداد Handlers ========
def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("reply", reply_command))

    # رسائل زر "📲 إظهار القائمة"
    app.add_handler(MessageHandler(filters.Regex("^📲 إظهار القائمة$"), handle_reply_buttons))

    # باقي الرسائل النصية
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))


# ======== Webhook endpoint ========

@flask_app.route(f"/webhook/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), ptb_app.bot)
    asyncio.create_task(ptb_app.process_update(update))
    return "OK", 200
@flask_app.route("/")
def index():
    return "TENTH POWER BOT is Running!", 200


# ======== Main ========
if __name__ == "__main__":
    



    # إنشاء تطبيق Telegram
    ptb_app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    setup_handlers(ptb_app)
    # تهيئة التطبيق قبل Webhook
    asyncio.run(ptb_app.initialize())
    asyncio.run(ptb_app.start())

    # تشغيل Webhook أو Polling حسب الإعداد
    if WEBHOOK_URL:
        # ضبط Webhook
        asyncio.run(ptb_app.bot.set_webhook(url=f"{WEBHOOK_URL}/webhook/{TELEGRAM_TOKEN}"))
        logger.info(f"Webhook set to {WEBHOOK_URL}/webhook/{TELEGRAM_TOKEN}")

        # تشغيل Flask
        port = int(os.environ.get("PORT", 10000))
        logger.info(f"Starting Flask app on port {port}")
        flask_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
    else:
        # إذا لم يكن Webhook محدد، شغّل Polling مباشر
        logger.info("No WEBHOOK_URL set. Running in polling mode.")
        asyncio.run(ptb_app.run_polling())
