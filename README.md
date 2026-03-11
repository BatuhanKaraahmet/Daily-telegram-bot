# 📱 Daily Telegram Bot

Her sabah otomatik Telegram mesajı gönderen Python bot. GitHub Actions ile tamamen ücretsiz ve sunucusuz çalışır.

## ✨ Özellikler

- 🕗 Her sabah saat 08:00'de otomatik mesaj
- ☁️ GitHub Actions ile bulutta çalışır (sunucu gerekmez)
- 🔒 Güvenli (Token'lar GitHub Secrets'ta)
- 💰 Tamamen ücretsiz
- ⚡ Kolay kurulum (5-10 dakika)

## 🚀 Hızlı Başlangıç

Detaylı kurulum için → **[KURULUM.md](KURULUM.md)** dosyasını okuyun.

### Kısa Özet:

1. **Bot oluştur:** Telegram'da @BotFather → TOKEN al
2. **Botu aktif et:** Mesaj alacak kişi `/start` yapsın
3. **Chat ID bul:** `https://api.telegram.org/bot<TOKEN>/getUpdates`
4. **Secrets ekle:** GitHub repo → Settings → Secrets
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
5. **Test et:** Actions → Run workflow

## 📁 Proje Yapısı

```
Daily-telegram-bot/
├── bot.py                      # Ana Python kodu
├── requirements.txt            # Gerekli paketler
├── .github/
│   └── workflows/
│       └── daily-telegram.yml  # GitHub Actions yapılandırması
├── KURULUM.md                  # Detaylı kurulum rehberi
└── README.md                   # Bu dosya
```

## 🔧 Teknolojiler

- **Python 3.11** - Bot kodu
- **requests** - Telegram API
- **GitHub Actions** - Otomasyon
- **Telegram Bot API** - Mesajlaşma

## 📝 Mesajı Özelleştirme

`bot.py` içindeki `message` değişkenini düzenleyin:

```python
message = f"""
🌅 Günaydın!

📅 Tarih: {today}

Kendi mesajınızı yazın! 💪
"""
```

## ⏰ Zamanlamayı Değiştirme

`.github/workflows/daily-telegram.yml` dosyasındaki cron değerini düzenleyin:

```yaml
schedule:
  - cron: '0 5 * * *'  # 08:00 Türkiye (UTC+3)
```

## 📄 Lisans

MIT License - İstediğiniz gibi kullanabilirsiniz.

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!

## ❓ Sorun mu var?

[KURULUM.md](KURULUM.md) dosyasındaki **"Sık Sorulan Sorular"** bölümüne bakın.
