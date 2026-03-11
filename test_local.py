"""
Lokal test için bu dosyayı kullanın.
Bu dosya .env dosyasından değişkenleri okur ve botu test eder.

Kullanım:
1. .env.example dosyasını .env olarak kopyalayın
2. .env içine kendi token, chat_id ve mesajınızı yazın
3. python test_local.py komutunu çalıştırın
"""

from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# bot.py'deki fonksiyonu kullan
from bot import send_telegram_message

if __name__ == "__main__":
    print("🧪 Lokal test başlıyor...")
    print(f"Token var mı: {'✅' if os.getenv('TELEGRAM_BOT_TOKEN') else '❌'}")
    print(f"Chat ID var mı: {'✅' if os.getenv('TELEGRAM_CHAT_ID') else '❌'}")
    print(f"Özel mesaj var mı: {'✅' if os.getenv('TELEGRAM_MESSAGE') else '❌ (Varsayılan kullanılacak)'}")
    print("\n" + "="*50 + "\n")
    
    send_telegram_message()
