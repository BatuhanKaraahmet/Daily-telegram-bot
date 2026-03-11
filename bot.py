import os
import requests
from datetime import datetime

def send_telegram_message():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    message_template = os.environ.get('TELEGRAM_MESSAGE')
    
    if not token or not chat_id:
        print("❌ HATA: TELEGRAM_BOT_TOKEN veya TELEGRAM_CHAT_ID bulunamadı!")
        return
    
    # Mesaj içeriği (eğer TELEGRAM_MESSAGE yoksa varsayılan mesaj)
    today = datetime.now().strftime("%d.%m.%Y")
    
    if message_template:
        # {today} varsa tarihi yerleştir
        message = message_template.replace('{today}', today)
    else:
        # Varsayılan mesaj
        message = f"""🌅 Günaydın!

📅 Tarih: {today}

Harika bir gün geçirmenizi dilerim! 💪"""
    
    # Telegram API'ye istek
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Mesaj başarıyla gönderildi!")
            print(f"Chat ID: {chat_id}")
        else:
            print(f"Mesaj gönderilemedi. HTTP {response.status_code}")
            print(f"Hata: {response.text}")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    send_telegram_message()
