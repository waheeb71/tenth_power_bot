# app.py
import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    Application
)

from handlers import start, setup_handlers

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
global ptb_application
# Flask App
flask_app = Flask(__name__)

# PTB Application (global)
ptb_application = None

@flask_app.route(f"/webhook/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
async def webhook():
    # استقبال التحديث كـ JSON
    json_str = request.get_json()
    update = Update.de_json(json_str, ptb_application.bot)
    
    # معالجة التحديث بشكل غير متزامن
    await ptb_application.process_update(update)
    
    return "OK", 200

@flask_app.route("/")
def index():
    return "TENTH POWER BOT is Running!", 200

if __name__ == "__main__":
    # بناء تطبيق PTB
    ptb_app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

    # إعداد المعالجات
    setup_handlers(ptb_app)

    # تعيينه كـ global
   
    ptb_application = ptb_app

    # تعيين Webhook إذا كان محددًا
    if os.getenv("WEBHOOK_URL"):
        webhook_url = f"{os.getenv('WEBHOOK_URL')}/webhook/{os.getenv('TELEGRAM_TOKEN')}"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ptb_app.bot.set_webhook(url=webhook_url))
        logger.info(f"✅ Webhook تم تعيينه: {webhook_url}")
    else:
        logger.warning("❌ لم يتم تعيين WEBHOOK_URL. تأكد من ضبطه.")

    # تشغيل Flask
    port = int(os.environ.get("PORT", 10000))
    logger.info(f"🚀 تشغيل البوت على المنفذ {port}")
    flask_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)