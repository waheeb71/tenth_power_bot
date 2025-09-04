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

# إعداد اللوجات
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app
flask_app = Flask(__name__)

# Telegram Application
ptb_application: Application = None
ptb_loop: asyncio.AbstractEventLoop = None


# إعداد الهاندلرز
def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reply", reply_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.Regex("^📲 إظهار القائمة$"), handle_reply_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Debug لكل تحديث
    async def log_all(update: Update, context):
        logger.info(f"📩 Received update: {update.to_dict()}")

    app.add_handler(MessageHandler(filters.ALL, log_all))


# Route للويبهوك
@flask_app.route(f"/webhook/{os.getenv('TELEGRAM_TOKEN')}", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, ptb_application.bot)

    # Debug log
    print("📩 Received update:", update.to_dict())

    # مرر التحديث للـ Application
    asyncio.run_coroutine_threadsafe(
        ptb_application.process_update(update),
        ptb_loop   # ✅ استخدم ptb_loop
    )
    return "OK", 200


@flask_app.route("/")
def index():
    return "TENTH POWER BOT is Running!", 200

if __name__ == "__main__":
    # إنشاء التطبيق
    ptb_app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    setup_handlers(ptb_app)

    # هاندلر اختبار (echo)
    async def echo(update: Update, context):
        await update.message.reply_text(f"👋 انت قلت: {update.message.text}")

    ptb_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    ptb_application = ptb_app
