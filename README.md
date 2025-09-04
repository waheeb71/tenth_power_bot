# Business Assistant Bot\<div align="center"\>

  \<h3\>Smart Telegram Bot for Customer Management and Automated Customer Service\</h3\>
  \<p\>Powered by \<strong\>Google Gemini\</strong\> | Perfect for Businesses, Contractors, and Technical Services\</p\>

  \<a href="[https://t.me/Ponamohabot](https://t.me/Ponamohabot)" target="\_blank"\>
    \<img src="[https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)" alt="Bot Link"\>
  \</a\>
  \<a href="[https://github.com/waheeb71/tenth\_power\_bot/blob/main/LICENSE](https://github.com/waheeb71/tenth_power_bot/blob/main/LICENSE)"\>
    \<img src="[https://img.shields.io/badge/License-MIT-green.svg](https://img.shields.io/badge/License-MIT-green.svg)" alt="License"\>
  \</a\>
  \<a href="[https://github.com/waheeb71/tenth\_power\_bot/stargazers](https://github.com/waheeb71/tenth_power_bot/stargazers)"\>
    \<img src="[https://img.shields.io/github/stars/waheeb71/tenth\_power\_bot?style=social](https://img.shields.io/github/stars/waheeb71/tenth_power_bot?style=social)" alt="Stars"\>
  \</a\>

\</div\>

-----

## Overview

**Business Assistant Bot** is an integrated Telegram bot designed to help small and medium-sized businesses automatically manage customer communication using artificial intelligence and human interaction.

It combines:

  - Smart responses via **Google Gemini**
  - An interactive button interface
  - A message forwarding system for admins with direct reply capability
  - 🌐 **Webhook** support for deployment on Render / Heroku / Railway

Ideal for businesses in the following fields:

  - Contracting
  - Maintenance and technical services
  - Administrative services
  - 🔧 Technical support

-----

## Key Features

| Feature | Description |
|-------|-------|
| 💡 Smart Responses | Uses **Google Gemini 1.5 Flash** for automatic replies in Arabic and English |
| 📱 Interactive User Interface | Main buttons for services, contact, and consultations |
| 📥 Internal Messaging System | A client can send a message, and admins are notified |
| ✉️ Team Reply | The admin replies using the `/reply_123` command, and the response is automatically sent to the client |
| 🌐 Webhook and Polling Support | Works in local and public server environments |
| 🔧 Easy to Customize | Texts, services, and contact numbers can be easily modified |
| 📦 Lightweight and Fast | Built on `python-telegram-bot` and `Flask` |

-----

## Technical Structure

```
business-assistant-bot/
├── app.py               # Main application (Flask + PTB)
├── ai_handler.py        # Connection to Gemini API
├── handlers.py          # Commands and buttons
├── config.py            # General settings
├── requirements.txt     # Required libraries
└── README.md            # This file
```

-----

## 🔧 Requirements

  - ✅ Python 3.8 or newer
  - ✅ [Google Gemini API Key](https://aistudio.google.com/app/apikey)
  - ✅ [Telegram Bot Token](https://t.me/BotFather)
  - ✅ A server that supports HTTPS (such as Render, Heroku, or VPS) — to enable Webhook

-----

## How to Run

### 1\. Clone the project

```bash
git clone https://github.com/waheeb71/tenth_power_bot.git
cd tenth_power_bot
```

### 2\. Install dependencies

```bash
pip install -r requirements.txt
```

### 3\. Set environment variables

Create a `.env` file or set the variables directly in the environment:

```bash
export TELEGRAM_TOKEN="123456:ABC-DEF123456"
export GEMINI_API_KEY="AIzaSyXXXXXXYourKeyHere"
export WEBHOOK_URL="https://yourdomain.onrender.com"  # Leave empty for local running
export PORT=10000
```

> ⚠️ Use `https://` only in `WEBHOOK_URL`.

### 4\. Run

```bash
python app.py
```

> If you don't enable webhook, the bot will automatically run using the **polling** system.

-----

## 🌐 Deployment on Render / Heroku

1.  Upload the project to a GitHub repository.
2.  Create an application on [Render](https://render.com) or Heroku.
3.  Link it to the repository.
4.  Add the environment variables in the dashboard.
5.  Run the application.

✅ The Webhook will be set automatically.

-----

## How to Customize

1.  Open the `config.py` file and edit:
       - `COMPANY_NAME`: Your company name
       - `CONTACT_PHONE`: Contact number
       - `CONTACT_EMAIL`: Company email
       - `SERVICES`: List of services
       - `ADMIN_IDS`: Telegram admin IDs

2.  Edit the texts in `handlers.py` according to your business's nature.

-----

## License

This project is distributed under the [MIT](https://www.google.com/search?q=LICENSE) license, which means you can:

  - Reuse it
  - Modify it
  - Sell it as part of a service
  - Use it commercially

-----

\<div align="center"\>
  \<p\>Built to empower businesses to automate customer service efficiently and intelligently.\</p\>
  \<p\>Contribute to its development or share it with your team\!\</p\>
  \<img src="[https://img.icons8.com/ios-filled/50/000000/globe.png](https://img.icons8.com/ios-filled/50/000000/globe.png)" alt="World" width="30"/\>
\</div\>

```

-----

## How to Benefit from This Project

  - ✔️ Use it as a **ready-made template** for any company.
  - ✔️ Add it to your project portfolio as a **smart customer management system**.
  - ✔️ Sell it as a service to small businesses.
  - ✔️ Add a web panel for admins to turn it into a full CRM system.

-----

## Contact:

For questions or support, contact me via:

  - Telegram: [@SyberSc71](https://t.me/SyberSc71)
  - Telegram: [@WAT4F](https://t.me/WAT4F)
  - GitHub: [waheeb71](https://github.com/waheeb71)
  - GitHub2: [cyberlangdev](https://github.com/cyberlangdev)
  - **Location:** I am from Yemen, Taiz.
  - **YouTube Channel:** [Cyber Code](https://www.youtube.com/@cyber_code1)
  - **X (formerly Twitter):** [@wa\_\_cys](https://x.com/wa__cys)

-----

## Author

**English:** Waheeb Mahyoob Al-Sharabi (Waheeb Al-Sharabi)  
**Arabic:** وهيب مهيوب الشرعبي (وهيب الشرعبي )
```

## اللغة / Language

📖 [اقرأ النسخة العربية](READMEAR.md)

