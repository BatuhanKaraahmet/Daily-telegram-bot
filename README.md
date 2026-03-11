# 📱 Daily Telegram Bot

Her sabah otomatik Telegram mesajı gönderen Python bot. GitHub Actions ile tamamen ücretsiz ve sunucusuz çalışır.

## ✨ Özellikler

- 🕗 Her sabah saat 08:00'de otomatik mesaj
- ☁️ GitHub Actions ile bulutta çalışır (sunucu gerekmez)
- 🔒 Güvenli (Token'lar ve mesajlar GitHub Secrets'ta)
- 💰 Tamamen ücretsiz
- ⚡ Kolay kurulum (5-10 dakika)
- 🔐 Mesajınız gizli kalır (repo public olsa bile)

## 🚀 Hızlı Başlangıç

Detaylı kurulum için → **[KURULUM.md](KURULUM.md)** dosyasını okuyun.

### Kısa Özet:

1. **Bot oluştur:** Telegram'da @BotFather → TOKEN al
2. **Botu aktif et:** Mesaj alacak kişi `/start` yapsın
3. **Chat ID bul:** `https://api.telegram.org/bot<TOKEN>/getUpdates`
4. **Secrets ekle:** GitHub repo → Settings → Secrets
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `TELEGRAM_MESSAGE` ← **Mesajınız (gizli)**
5. **Test et:** Actions → Run workflow

## 📁 Proje Yapısı

```
Daily-telegram-bot/
├── bot.py                      # Ana Python kodu
├── test_local.py               # Lokal test dosyası
├── requirements.txt            # Gerekli paketler
├── .env.example                # Örnek environment dosyası
├── .github/
│   └── workflows/
│       └── daily-telegram.yml  # GitHub Actions yapılandırması
├── KURULUM.md                  # Detaylı kurulum rehberi
├── GIZLILIK.md                 # Gizlilik ve güvenlik rehberi
└── README.md                   # Bu dosya
```

## 🔧 Teknolojiler

- **Python 3.11** - Bot kodu
- **requests** - Telegram API
- **python-dotenv** - Environment variable yönetimi
- **GitHub Actions** - Otomasyon
- **Telegram Bot API** - Mesajlaşma

## 🔐 Gizlilik ve Güvenlik

**Mesajınız kodda görünmez!** Tüm gizli bilgiler güvenli şekilde saklanır:

- ✅ Token'lar şifreli (GitHub Secrets)
- ✅ Chat ID şifreli (GitHub Secrets)
- ✅ **Mesajınız şifreli** (GitHub Secrets)
- ✅ Public repo olsa bile kimse göremez

Detaylı bilgi için → **[GIZLILIK.md](GIZLILIK.md)**

## 📝 Mesajı Özelleştirme

Mesajınızı **GitHub Secrets**'ta değiştirin:

1. Settings → Secrets and variables → Actions
2. `TELEGRAM_MESSAGE` → Update
3. Yeni mesajınızı yazın

**Mesaj formatı:**
```
🌅 Günaydın!

📅 Tarih: {today}

İstediğiniz mesajı yazın! 💪
```

`{today}` yazarsanız otomatik tarih eklenir (örn: 11.03.2026)

## ⏰ Zamanlamayı Değiştirme

`.github/workflows/daily-telegram.yml` dosyasındaki cron değerini düzenleyin:

```yaml
schedule:
  - cron: '0 5 * * *'  # 08:00 Türkiye (UTC+3)
```

## 🧪 Lokal Test

```bash
# .env.example'ı kopyala
cp .env.example .env

# .env dosyasını düzenle (token, chat_id, mesaj ekle)
# ...

# Gereksinimleri yükle
pip install -r requirements.txt

# Test et
python test_local.py
```

## 📄 Lisans

MIT License - İstediğiniz gibi kullanabilirsiniz.

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!

## ❓ Sorun mu var?

- [KURULUM.md](KURULUM.md) - Adım adım kurulum
- [GIZLILIK.md](GIZLILIK.md) - Gizlilik ve güvenlik

## 🔒 Güvenlik Notu

**ÖNEMLİ:** `.env` dosyanız `.gitignore` içinde ve GitHub'a gitmez. Token'larınızı ve mesajınızı asla kodda yazmayın!
