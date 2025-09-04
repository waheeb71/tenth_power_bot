# Business Assistant Bot

<div align="center">

  <h3>Smart Telegram Bot for Customer Management and Automated Customer Service</h3>
  <p>Powered by <strong>Google Gemini</strong> | Ideal for businesses, contractors, and technical services</p>

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

## Overview

**Business Assistant Bot** is an integrated Telegram bot designed to help small and medium-sized businesses automatically manage customer communication, combining AI with human interaction.

It combines:
- Smart replies via **Google Gemini**
- Interactive button interface
- Supervisor message forwarding system with direct reply capability
- 🌐 **Webhook** support for deployment on Render / Heroku / Railway

Ideal for businesses in:
- Contracting
- Maintenance and technical services
- Administrative services
- 🔧 Technical support

---

## Key Features

| Feature | Description |
|-------|-------|
| 💡 Smart Replies | Uses **Google Gemini 1.5 Flash** for automatic responses in Arabic and English |
| 📱 Interactive UI | Main buttons for services, contact, and consultations |
| 📥 Internal Messaging System | Customers can send messages, and supervisors are notified |
| ✉️ Team Response | Supervisors reply using `/reply_123` command, and the response is automatically delivered to the customer |
| 🌐 Webhook and Polling Support | Works in local environments and public servers |
| 🔧 Easy Customization | Easily modify texts, services, and contact numbers |
| 📦 Lightweight and Fast | Built on `python-telegram-bot` and `Flask` |

---

## Technical Structure

```
business-assistant-bot/
├── app.py               # Main application (Flask + PTB)
├── ai_handler.py        # Google Gemini API integration
├── handlers.py          # Commands and button handlers
├── config.py            # General settings
├── requirements.txt     # Required libraries
└── README.md            # This file
```

---

## 🔧 Requirements

- ✅ Python 3.8 or higher
- ✅ [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- ✅ [Telegram Bot Token](https://t.me/BotFather)
- ✅ HTTPS-enabled server (e.g., Render, Heroku, or VPS) — for Webhook activation

---

## How to Run

### 1. Clone the Project
```bash
git clone https://github.com/waheeb71/tenth_power_bot.git
cd tenth_power_bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file or set variables directly in your environment:

```bash
export TELEGRAM_TOKEN="123456:ABC-DEF123456"
export GEMINI_API_KEY="AIzaSyXXXXXXYourKeyHere"
export WEBHOOK_URL="https://yourdomain.onrender.com"  # Leave empty for local polling
export PORT=10000
```

> ⚠️ Use `https://` only in `WEBHOOK_URL`.

### 4. Run the Bot
```bash
python app.py
```

> If webhook is not enabled, the bot will automatically run in **polling** mode.

---

## 🌐 Deployment on Render / Heroku

1. Push the project to a GitHub repository.
2. Create an app on [Render](https://render.com) or Heroku.
3. Connect it to your repository.
4. Add environment variables in the dashboard.
5. Launch the app.

✅ Webhook will be set automatically.

---

## How to Customize

1. Open `config.py` and modify:
   - `COMPANY_NAME`: Your company name
   - `CONTACT_PHONE`: Contact phone number
   - `CONTACT_EMAIL`: Company email
   - `SERVICES`: List of services
   - `ADMIN_IDS`: Telegram user IDs of supervisors

2. Edit texts in `handlers.py` according to your business needs.

---

## License

This project is distributed under the [MIT License](LICENSE), meaning you can:
- Reuse it
- Modify it
- Sell it as part of a service
- Use it commercially

---

<div align="center">
  <p>Built to empower businesses with efficient and intelligent customer service automation.</p>
  <p>Contribute to its development or share it with your team!</p>
  <img src="https://img.icons8.com/ios-filled/50/000000/globe.png" alt="World" width="30"/>
</div>

---

## How Can You Benefit From This Project?

- ✔️ Use it as a **ready-made template** for any business.
- ✔️ Include it in your portfolio as a **smart customer management system**.
- ✔️ Sell it as a service to small businesses.
- ✔️ Add a web dashboard for supervisors to turn it into a full CRM system.

---

## Contact:
For questions or support, contact me via:
- Telegram: [@SyberSc71](https://t.me/SyberSc71)
- Telegram: [@WAT4F](https://t.me/WAT4F)
- GitHub: [waheeb71](https://github.com/waheeb71)
- GitHub2: [cyberlangdev](https://github.com/cyberlangdev)
- **Location:** I am from Yemen, Taiz.
- **YouTube Channel:** [Cyber Code](https://www.youtube.com/@cyber_code1)
- **X (formerly Twitter):** [@wa__cys](https://x.com/wa__cys)

---

## Author / Developer

**English:** Waheeb Mahyoob Al-Sharabi (Waheeb Al-Sharabi)  
**العربية:** وهيب مهيوب الشرعبي (وهيب الشرعبي)

## اللغة / Language

📖 [اقرأ النسخة العربية](READMEAR.md)

