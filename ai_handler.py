# ai_handler.py
import requests
import json
from config import (
    GEMINI_API_KEY, COMPANY_NAME, CONTACT_PHONE, CONTACT_EMAIL,
    CONTACT_LOCATION, SERVICES, FACEBOOK_URL, INSTAGRAM_URL,
    TELEGRAM_URL, WHATSAPP_URL, SNAPCHAT_URL, TIKTOK_URL, WEBSITE_URL
)

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def get_ai_response(user_message: str) -> str:
    services_list = ", ".join(SERVICES)
    
    prompt = f"""
أنت TENTH POWER BOT، مساعد ذكي لشركة '{COMPANY_NAME}'، شركة رائدة في مجال المقاولات العامة والزجاج والألمنيوم وأعمال الاستانلس ستيل في المملكة العربية السعودية.

المؤسسة توفر الخدمات التالية: {services_list}

للتواصل:
- الهاتف: {CONTACT_PHONE}
- البريد الإلكتروني: {CONTACT_EMAIL}
- الموقع: {CONTACT_LOCATION}
- فيسبوك: {FACEBOOK_URL}
- إنستغرام: {INSTAGRAM_URL}
- تيليجرام: {TELEGRAM_URL}
- واتساب: {WHATSAPP_URL}
- سناب شات: {SNAPCHAT_URL}
- تيك توك: {TIKTOK_URL}
- الموقع الإلكتروني: {WEBSITE_URL}

الردود يجب أن تكون:
- بلغة المستخدم (عربي/إنجليزي)
- ارسل معرف التلجرام حق الملك اذا احب يتوصل تلجرام  وارسل له مواقع التواصل الاخرى او الرقم 
- مختصرة (2-3 جمل)
- ودودة، احترافية، وواثقة
- لا تختلق معلومات. إذا لم تكن متأكدًا، اطلب من المستخدم الاتصال بالفريق.



السياق: {user_message}
"""

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.5,
            "topK": 40,
            "topP": 0.9,
            "maxOutputTokens": 250
        }
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(data), timeout=30)
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            error_msg = response.json().get("error", {}).get("message", "خطأ في الاتصال بـ Gemini")
            print(f"Gemini API Error: {error_msg}")
            return f"عذرًا، لا يمكنني الرد حاليًا. يرجى المحاولة لاحقًا أو الاتصال بنا على {CONTACT_PHONE}."
    except Exception as e:
        print(f"Exception in Gemini request: {e}")
        return f"عذرًا، حدث خطأ تقني. يرجى التواصل معنا على {CONTACT_PHONE} أو {CONTACT_EMAIL}."
