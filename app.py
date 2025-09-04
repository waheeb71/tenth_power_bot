import os
import logging
import asyncio
from threading import Thread
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

from handlers import start, button_handler, message_handler, handle_reply_buttons

# إعداد اللوجات
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app
flask_app = Flask(__name__)

# Telegram Application
ptb_application: Application = None
main_event_loop: asyncio.AbstractEventLoop = None


# إعداد الهاندلرز
def setup_handlers(app: Application):
    """إعداد جميع المعالجات (handlers) للبوت."""
    app.add_handler(CommandHandler("start", start))
    
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.Regex("^📲 إظهار القائمة$"), handle_reply_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Debug لكل تحديث
    async def log_all(update: Update, context):
        logger.info(f"📩 Received update: {update.to_dict()}")

    app.add_handler(MessageHandler(filters.ALL, log_all))
    logger.info("تم إعداد جميع معالجات PTB.")


# Route للويبهوك
@flask_app.route(f"/webhook/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    """معالجة تحديثات تيليجرام الواردة عبر الويبهوك."""
    if not ptb_application or not main_event_loop or not main_event_loop.is_running():
        logger.error("تطبيق البوت أو دورة الحدث الخاصة به غير جاهزة للويبهوك.")
        return "Internal Server Error: Bot not ready", 500

    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, ptb_application.bot)
        
        # Debug log
        logger.info("📩 Received update:", update.to_dict())

        # مرر التحديث للـ Application في خيطها الخاص
        asyncio.run_coroutine_threadsafe(ptb_application.process_update(update), main_event_loop)
    except Exception as e:
        logger.error(f"حدث خطأ أثناء معالجة التحديث في الويبهوك: {e}", exc_info=True)
        return "Internal Server Error", 500
        
    return "ok", 200


@flask_app.route("/")
def index():
    return "TENTH POWER BOT is Running!", 200


def run_ptb_in_thread(app: Application, loop: asyncio.AbstractEventLoop):
    """تشغيل تطبيق البوت في خيط منفصل."""
    global main_event_loop
    main_event_loop = loop

    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(app.initialize())
        logger.info("تم تهيئة تطبيق البوت.")
        
        if os.getenv("WEBHOOK_URL"):
            full_webhook_url = f"{os.getenv('WEBHOOK_URL')}/webhook/{os.getenv('TELEGRAM_TOKEN')}"
            loop.run_until_complete(app.bot.set_webhook(url=full_webhook_url))
            logger.info(f"✅ تم تعيين الويبهوك إلى {full_webhook_url}")
            loop.run_forever()
        else:
            logger.error("⚠️ يجب تحديد WEBHOOK_URL في الـ Environment variables")
            # يمكن تشغيله في وضع polling هنا إذا لزم الأمر
    finally:
        if loop.is_running():
            loop.run_until_complete(app.shutdown())
        loop.close()

if __name__ == "__main__":
    # إنشاء التطبيق
    ptb_app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    setup_handlers(ptb_app)

    ptb_application = ptb_app

    # إعداد وتشغيل البوت في خيط منفصل
    ptb_event_loop = asyncio.new_event_loop()
    ptb_thread = Thread(target=run_ptb_in_thread, args=(ptb_application, ptb_event_loop), name="PTBThread")
    ptb_thread.daemon = True
    ptb_thread.start()
    logger.info("تم تشغيل خيط البوت.")

    # تشغيل Flask في الخيط الرئيسي
    port = int(os.environ.get("PORT", 10000))
    logger.info(f"🚀 Starting Flask app on port {port}")
    flask_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
