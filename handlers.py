from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from ai_handler import get_ai_response
from config import COMPANY_NAME, CONTACT_PHONE, CONTACT_EMAIL, CONTACT_LOCATION, SERVICES, ADMIN_IDS,FACEBOOK_URL,INSTAGRAM_URL,TELEGRAM_URL,WHATSAPP_URL,SNAPCHAT_URL,TIKTOK_URL,WEBSITE_URL

import logging

logger = logging.getLogger(__name__)

user_messages = {}

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📋 الخدمات", callback_data="services")],
        [InlineKeyboardButton("📞 اتصل بنا", callback_data="contact")],
        [InlineKeyboardButton("💬 استشارة فنية", callback_data="consult")],
        [InlineKeyboardButton("📩 إرسال رسالة للمشرف", callback_data="send_admin")],
        [InlineKeyboardButton("تابعنا على السوشيال", callback_data="social")],
        [InlineKeyboardButton("الموقع الإلكتروني", url="https://stunning-bubblegum-f108c3.netlify.app/")],
        [InlineKeyboardButton("رجوع", callback_data="show_main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)

def main_menu_reply():
    keyboard = [
        [KeyboardButton("📲 إظهار القائمة")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"مرحبًا بك في {COMPANY_NAME}!\n"
        "نقدم حلولًا متكاملة في الزجاج، الألمنيوم، والمقاولات العامة.\n"
        "اضغط الزر أدناه لعرض القائمة 👇",
        reply_markup=main_menu_reply()
    )

async def handle_reply_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "📲 إظهار القائمة":
        await update.message.reply_text(
            "اختر من القائمة:",
            reply_markup=main_menu()
        )

social_buttons = [
    [InlineKeyboardButton("فيسبوك", url=FACEBOOK_URL)],
    [InlineKeyboardButton("إنستغرام", url=INSTAGRAM_URL)],
    [InlineKeyboardButton("تيليجرام", url=TELEGRAM_URL)],
    [InlineKeyboardButton("واتساب", url=WHATSAPP_URL)],
    [InlineKeyboardButton("سناب شات", url=SNAPCHAT_URL)],
    [InlineKeyboardButton("تيك توك", url=TIKTOK_URL)],
    [InlineKeyboardButton("الموقع الإلكتروني", url=WEBSITE_URL)],
]

social_menu = InlineKeyboardMarkup(social_buttons)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "services":
        services_list = "\n".join(f"• {service}" for service in SERVICES)
        await query.edit_message_text(
            f"🔹 خدماتنا:\n{services_list}\n\nنضمن الجودة، الموثوقية، والابتكار في كل مشروع.",
            reply_markup=main_menu()
        )
    elif query.data == "contact":
        await query.edit_message_text(
            f"📞 الهاتف: {CONTACT_PHONE}\n"
            f"📧 البريد: {CONTACT_EMAIL}\n"
            f"📍 الموقع: {CONTACT_LOCATION}\n\n"
            "يمكنك الاتصال بنا على مدار الساعة!",
            reply_markup=main_menu()
        )
    elif query.data == "social":
        await query.edit_message_text(
            "تابعنا على مواقع التواصل الاجتماعي:",
            reply_markup=social_menu
        )
    elif query.data == "consult":
        await query.edit_message_text(
            "اكتب سؤالك أو استفسارك، وسأجيبك فورًا باستخدام الذكاء الاصطناعي.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 العودة", callback_data="show_main_menu")
            ]])
        )
        context.user_data['awaiting_ai_query'] = True
    elif query.data == "send_admin":
        await query.edit_message_text(
            "اكتب رسالتك للمشرفين وسيتم الرد عليك قريبًا.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 العودة", callback_data="show_main_menu")
            ]])
        )
        context.user_data['awaiting_admin_msg'] = True
    elif query.data == "show_main_menu":
        await query.edit_message_text("اختر من القائمة:", reply_markup=main_menu())

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if context.user_data.get('awaiting_ai_query'):
        try:
            response = get_ai_response(text)
            if response:
                await update.message.reply_text(response)
            else:
                await update.message.reply_text("عذراً، لم أستطع الحصول على إجابة. يرجى المحاولة لاحقاً.")
        except Exception as e:
            logger.error(f"Error in AI handler: {e}")
            await update.message.reply_text("حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى.")
        
        del context.user_data['awaiting_ai_query']
        await update.message.reply_text("العودة للقائمة:", reply_markup=main_menu())
        return

    if context.user_data.get('awaiting_admin_msg'):
        msg_id = update.message.message_id
        user_messages[msg_id] = (user_id, text)

        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=f"📩 رسالة من عميل (ID: {user_id}):\n{text}\n\n"
                         f"استخدم /reply_{msg_id} للرد على هذه الرسالة."
                )
            except Exception as e:
                logger.error(f"فشل إرسال للمشرف {admin_id}: {e}")

        await update.message.reply_text(
            "تم إرسال رسالتك بنجاح! سيتواصل معك أحد المشرفين قريبًا.",
            reply_markup=main_menu()
        )
        del context.user_data['awaiting_admin_msg']
        return

    # Fallback to AI response for any other text
    try:
        response = get_ai_response(text)
        if response:
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("عذراً، لم أستطع فهم طلبك. يرجى استخدام القائمة الرئيسية.")
    except Exception as e:
        logger.error(f"Error in AI handler for fallback: {e}")
        await update.message.reply_text("حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى.")

async def reply_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("غير مصرح لك باستخدام هذا الأمر.")
        return

    try:
        command_args = context.args
        if not command_args:
            await update.message.reply_text("استخدم: `/reply_MESSAGE_ID <نص الرد>`")
            return
        
        full_command = command_args[0]
        if not full_command.startswith("reply_"):
            await update.message.reply_text("صيغة الأمر غير صحيحة. استخدم: `/reply_MESSAGE_ID <نص الرد>`")
            return
        
        msg_id = int(full_command.split("_")[1])
    except (IndexError, ValueError):
        await update.message.reply_text("صيغة الأمر غير صحيحة. استخدم: `/reply_MESSAGE_ID <نص الرد>`")
        return

    if msg_id not in user_messages:
        await update.message.reply_text("الرسالة غير موجودة.")
        return

    user_id, original_text = user_messages[msg_id]
    reply_text = " ".join(command_args[1:])

    if not reply_text:
        await update.message.reply_text("يجب إدخال نص للرد.")
        return

    try:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"📩 رد من المشرف:\n{reply_text}\n\nشكرًا لتواصلك مع {COMPANY_NAME}."
        )
        await update.message.reply_text("✅ تم إرسال الرد بنجاح!")
    except Exception as e:
        await update.message.reply_text(f"فشل الإرسال: {str(e)}")
