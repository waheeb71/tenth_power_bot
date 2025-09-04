# handlers.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from ai_handler import get_ai_response
from config import COMPANY_NAME, CONTACT_PHONE, CONTACT_EMAIL, CONTACT_LOCATION, SERVICES, ADMIN_IDS, FACEBOOK_URL, INSTAGRAM_URL, TELEGRAM_URL, WHATSAPP_URL, SNAPCHAT_URL, TIKTOK_URL, WEBSITE_URL

user_messages = {}  # لتخزين رسائل العملاء

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📋 الخدمات", callback_data="services")],
        [InlineKeyboardButton("📞 اتصل بنا", callback_data="contact")],
        [InlineKeyboardButton("💬 استشارة فنية", callback_data="consult")],
        [InlineKeyboardButton("📩 إرسال رسالة للمشرف", callback_data="send_admin")],
        [InlineKeyboardButton("تابعنا على السوشيال", callback_data="social")],
        [InlineKeyboardButton("الموقع الإلكتروني", url=WEBSITE_URL)],
        [InlineKeyboardButton("رجوع", callback_data="back")],
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

# التعامل مع زر "📲 إظهار القائمة"
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
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 العودة", callback_data="back")]])
        )
        context.user_data['awaiting_ai_query'] = True

    elif query.data == "send_admin":
        await query.edit_message_text(
            "اكتب رسالتك للمشرفين وسيتم الرد عليك قريبًا.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 العودة", callback_data="back")]])
        )
        context.user_data['awaiting_admin_msg'] = True

    elif query.data.startswith("admin_reply_"):
        # وضع المشرف في حالة انتظار الرد على رسالة معينة
        msg_id = int(query.data.split("_")[-1])
        context.user_data['reply_to_msg'] = msg_id
        await query.message.reply_text("📩 اكتب ردك الآن:")

    elif query.data == "back":
        await query.edit_message_text("اختر من القائمة:", reply_markup=main_menu())

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # حالة الرد على استفسار الذكاء الاصطناعي
    if context.user_data.get('awaiting_ai_query'):
        response = get_ai_response(text)
        await update.message.reply_text(response)
        del context.user_data['awaiting_ai_query']
        await update.message.reply_text("العودة للقائمة:", reply_markup=main_menu())
        return

    # حالة إرسال رسالة للمشرف
    if context.user_data.get('awaiting_admin_msg'):
        msg_id = update.message.message_id
        user_messages[msg_id] = (user_id, text)

        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    chat_id=admin_id,
                    text=f"📩 رسالة من عميل (ID: {user_id}):\n{text}",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔁 رد على الرسالة", callback_data=f"admin_reply_{msg_id}")
                    ]])
                )
            except Exception as e:
                print(f"فشل إرسال للمشرف {admin_id}: {e}")

        await update.message.reply_text(
            "تم إرسال رسالتك بنجاح! سيتواصل معك أحد المشرفين قريبًا.",
            reply_markup=main_menu()
        )
        del context.user_data['awaiting_admin_msg']
        return

    # حالة المشرف يكتب الرد على رسالة العميل
    if 'reply_to_msg' in context.user_data:
        msg_id = context.user_data['reply_to_msg']
        if msg_id in user_messages:
            user_id, _ = user_messages[msg_id]
            await context.bot.send_message(
                chat_id=user_id,
                text=f"📩 رد من المشرف:\n{text}\n\nشكرًا لتواصلك مع {COMPANY_NAME}."
            )
            await update.message.reply_text("✅ تم إرسال الرد بنجاح!")
            del context.user_data['reply_to_msg']
        return

    # الرد الافتراضي باستخدام الذكاء الاصطناعي
    response = get_ai_response(text)
    await update.message.reply_text(response)
