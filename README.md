# 🤖 Business Assistant Bot

<div align="center">

  <h3>بوت تلجرام ذكي لإدارة العملاء وخدمة العملاء الآلية</h3>
  <p>مدعوم بـ <strong>Google Gemini</strong> | مثالي للشركات، المقاولين، والخدمات الفنية</p>

  <a href="https://t.me/Ponamohabot" target="_blank">
    <img src="https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram" alt="Bot Link">
  </a>
  <a href="https://github.com/waheeb71/tenth_power_bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
  <a href="https://github.com/waheeb71/tenth_power_bot/stargazers">
    <img src="https://img.shields.io/github/stars/waheeb71/tenth_power_bot?style=social" alt="Stars">
  </a>
</div>

---

##  نظرة عامة

**Business Assistant Bot** هو بوت تلجرام متكامل مصمم لمساعدة الشركات الصغيرة والمتوسطة على إدارة تواصل العملاء تلقائيًا، باستخدام الذكاء الاصطناعي والتفاعل البشري.

يجمع بين:
- 💬 الردود الذكية عبر **Google Gemini**
- 📋 واجهة أزرار تفاعلية
- 📩 نظام إرسال الرسائل للمشرفين مع إمكانية الرد المباشر
- 🌐 دعم **Webhook** للنشر على Render / Heroku / Railway

مثالي للشركات في مجالات:
- 🏗️ المقاولات
- 🛠️ الصيانة والخدمات الفنية
- 🏢 الخدمات الإدارية
- 🔧 الدعم الفني

---

## 🚀 الميزات الرئيسية

| الميزة | الوصف |
|-------|-------|
| 💡 ردود ذكية | باستخدام **Google Gemini 1.5 Flash** للإجابة التلقائية بالعربية والإنجليزية |
| 📱 واجهة مستخدم تفاعلية | أزرار رئيسية للخدمات، التواصل، والاستشارات |
| 📥 نظام الرسائل الداخلية | يستطيع العميل إرسال رسالة، ويتم تنبيه المشرفين |
| ✉️ الرد من الفريق | المشرف يرد عبر أمر `/reply_123` ويصل الرد تلقائيًا للعميل |
| 🌐 دعم Webhook وPolling | يعمل في البيئات المحلية والخوادم العامة |
| 🔧 سهل التخصيص | يمكن تعديل النصوص، الخدمات، وأرقام التواصل بسهولة |
| 📦 خفيف وسريع | مبني على `python-telegram-bot` و `Flask` |

---


##  الهيكل التقني

```
business-assistant-bot/
├── app.py               # التطبيق الرئيسي (Flask + PTB)
├── ai_handler.py        # الاتصال بـ Gemini API
├── handlers.py          # الأوامر والأزرار
├── config.py            # الإعدادات العامة
├── requirements.txt     # المكتبات المطلوبة
└── README.md            # هذا الملف
```

---

## 🔧 المتطلبات

- ✅ Python 3.8 أو أحدث
- ✅ [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- ✅ [Telegram Bot Token](https://t.me/BotFather)
- ✅ خادم يدعم HTTPS (مثل Render، Heroku، أو VPS) — لتفعيل Webhook

---

##  كيفية التشغيل

### 1. استنساخ المشروع
```bash
git clone https://github.com/waheeb71/tenth_power_bot.git
cd tenth_power_bot
```

### 2. تثبيت التبعيات
```bash
pip install -r requirements.txt
```

### 3. تعيين المتغيرات البيئية

أنشئ ملف `.env` أو عيّن المتغيرات مباشرة في البيئة:

```bash
export TELEGRAM_TOKEN="123456:ABC-DEF123456"
export GEMINI_API_KEY="AIzaSyXXXXXXYourKeyHere"
export WEBHOOK_URL="https://yourdomain.onrender.com"  # اتركه فارغًا للتشغيل المحلي
export PORT=10000
```

> ⚠️ استخدم `https://` فقط في `WEBHOOK_URL`.

### 4. التشغيل
```bash
python app.py
```

> إذا لم تُفعّل webhook، يعمل البوت بنظام **polling** تلقائيًا.

---

## 🌐 النشر على Render / Heroku

1. رفع المشروع إلى مستودع على GitHub.
2. إنشاء تطبيق على [Render](https://render.com) أو Heroku.
3. ربطه بالمستودع.
4. إضافة المتغيرات البيئية في لوحة التحكم.
5. تشغيل التطبيق.

✅ سيتم تعيين الـ Webhook تلقائيًا.

---

## 🛠️ كيفية التخصيص

1. افتح ملف `config.py` وعدّل:
   - `COMPANY_NAME`: اسم شركتك
   - `CONTACT_PHONE`: رقم التواصل
   - `CONTACT_EMAIL`: بريد الشركة
   - `SERVICES`: قائمة الخدمات
   - `ADMIN_IDS`: معرفات المشرفين في تلجرام

2. عدّل النصوص في `handlers.py` حسب طبيعة نشاطك.

---

## 📄 الترخيص

هذا المشروع مُوزَّع تحت ترخيص [MIT](LICENSE)، ما يعني أنه يمكنك:
- إعادة استخدامه
- تعديله
- بيعه كجزء من خدمة
- استخدامه تجاريًا

---

<div align="center">
  <p>🚀 تم بناؤه لتمكين الشركات من أتمتة خدمة العملاء بكفاءة وذكاء.</p>
  <p>ساهم في تطويره أو شاركه مع فريقك!</p>
  <img src="https://img.icons8.com/ios-filled/50/000000/globe.png" alt="World" width="30"/>
</div>
```

---

## ✅ كيف تستفيد من هذا المشروع؟

- ✔️ استخدمه كـ **قالب جاهز** لأي شركة.
- ✔️ أضفه إلى محفظة المشاريع كـ **نظام إدارة عملاء ذكي**.
- ✔️ بيعه كخدمة للشركات الصغيرة.
- ✔️ أضف لوحة ويب للمشرفين لتحويله إلى نظام CRM كامل.

---




##  Contact:
For questions or support, contact me via:
- Telegram: [@SyberSc71](https://t.me/SyberSc71)
- Telegram: [@WAT4F](https://t.me/WAT4F)
- GitHub: [waheeb71](https://github.com/waheeb71)
- GitHub2: [cyberlangdev](https://github.com/cyberlangdev)
- **Location:** I am from Yemen, Taiz.
- **YouTube Channel:** [Cyber Code](https://www.youtube.com/@cyber_code1)
- **X (formerly Twitter):** [@wa__cys](https://x.com/wa__cys)

---
## Author / المطور

**English:** Waheeb Mahyoob Al-Sharabi (Waheeb Al-Sharabi)  
**العربية:** وهيب مهيوب الشرعبي (وهيب الشرعبي )