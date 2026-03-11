# 📱 Telegram Bot Kurulum Rehberi

Bu rehber ile her sabah otomatik Telegram mesajı gönderen botu kuracaksınız.

---

## 🎯 1. ADIM: Telegram Botunu Oluştur

1. Telegram'da **@BotFather**'ı aç
2. `/newbot` komutunu gönder
3. **Bot adı** ver (örn: "Günlük Hatırlatıcı")
4. **Bot kullanıcı adı** ver (sonu `bot` ile bitmeli, örn: `batuhan_morning_bot`)
5. BotFather size bir **TOKEN** verecek → 📋 **Bunu kaydet!**

```
✅ Çıktı: TELEGRAM_BOT_TOKEN
Örnek: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

---

## 👤 2. ADIM: Mesaj Alacak Kişi Botu Aktif Etsin

**ÖNEMLİ:** Bu adım olmadan chat_id bulamazsınız!

1. Mesaj gidecek kişi Telegram'da botunuzu bulsun
2. **Start** tuşuna bassın (veya `/start` yazsın)
3. İsteğe bağlı bir mesaj yazsın

```
✅ Çıktı: Bot ile sohbet başladı
```

---

## 🔑 3. ADIM: CHAT_ID'yi Öğren

Tarayıcınızda şu adresi açın (TOKEN'ı kendi tokenınız ile değiştirin):

```
https://api.telegram.org/bot<TOKEN>/getUpdates
```

**Örnek:**
```
https://api.telegram.org/bot123456789:ABCdefGHI/getUpdates
```

Açılan JSON içinde şunu arayın:

```json
{
  "result": [{
    "message": {
      "chat": {
        "id": 123456789,  ← BU CHAT_ID
        "first_name": "Batuhan",
        ...
      }
    }
  }]
}
```

```
✅ Çıktı: TELEGRAM_CHAT_ID (sayısal)
Örnek: 123456789
```

**⚠️ Sorun mu var?** Eğer `result: []` görüyorsanız:
- Kişi botla henüz konuşmamış → Adım 2'yi tekrar yapın
- Sayfayı yenileyin

---

## 🔐 4. ADIM: GitHub Secrets'ı Ayarla

1. GitHub repo sayfanıza gidin
2. **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** butonuna tıklayın
4. İki secret ekleyin:

### Secret 1:
- **Name:** `TELEGRAM_BOT_TOKEN`
- **Secret:** `123456789:ABCdefGHIjklMNOpqrsTUVwxyz` (kendi tokenınız)

### Secret 2:
- **Name:** `TELEGRAM_CHAT_ID`
- **Secret:** `123456789` (kendi chat id'niz)

```
✅ Çıktı: Secrets güvenli şekilde saklandı
```

---

## 🧪 5. ADIM: İlk Testi Yap

1. GitHub repo'da **Actions** sekmesine git
2. Sol taraftan **"Daily Telegram Message"** workflow'unu seç
3. Sağ tarafta **"Run workflow"** → **"Run workflow"** tıkla
4. 10-20 saniye bekle
5. Telefonunuza mesaj geldi mi kontrol edin

```
✅ Başarılı: Mesaj geldi! 🎉
❌ Başarısız: Aşağıdaki kontrolleri yap
```

### ❌ Mesaj Gelmediyse:

1. **Actions** sekmesinde hata loglarını inceleyin
2. Yaygın hatalar:
   - ❌ Chat ID yanlış → Adım 3'ü tekrar yapın
   - ❌ Token yanlış → Adım 1'i kontrol edin
   - ❌ Bot start yapılmamış → Adım 2'yi tekrar yapın
   - ❌ Secrets yanlış yazılmış → TELEGRAM_BOT_TOKEN ve TELEGRAM_CHAT_ID ismini kontrol edin

---

## ⏰ 6. ADIM: Otomasyonu Doğrula

Artık bot **her sabah saat 08:00 (Türkiye)** otomatik çalışacak!

- GitHub Actions her gün sabah botunuzu çalıştırır
- Sunucu kiralama gerekmez
- Bilgisayarınız açık olmak zorunda değil
- Tamamen ücretsiz (Public repo)

```
✅ Sistem aktif! Yarın sabah mesaj gelecek
```

---

## 📝 Mesajı Özelleştirme

`bot.py` dosyasındaki `message` değişkenini düzenleyin:

```python
message = f"""
🌅 Günaydın!

📅 Tarih: {today}

İstediğiniz mesajı buraya yazın! 💪
"""
```

Değişiklik yaptıktan sonra:
```bash
git add .
git commit -m "Mesaj güncellendi"
git push
```

---

## ⏱️ Saati Değiştirme

`.github/workflows/daily-telegram.yml` dosyasındaki cron zamanlamasını düzenleyin:

```yaml
schedule:
  - cron: '0 5 * * *'  # 08:00 TR (05:00 UTC)
```

**Örnekler:**
- 07:00 TR → `'0 4 * * *'` (04:00 UTC)
- 09:00 TR → `'0 6 * * *'` (06:00 UTC)
- 20:00 TR → `'0 17 * * *'` (17:00 UTC)

**Not:** Türkiye UTC+3, yaz saatinde kontrol edin.

---

## ❓ Sık Sorulan Sorular

### Bot mesaj gönderiyor ama göndermiyor diyor?
- `getUpdates` ile chat_id'yi tekrar kontrol edin
- Botla tekrar `/start` yapın

### Actions çalışmıyor?
- Public repo mu kontrol edin
- Actions Settings → Actions permissions → "Allow all actions" seçili mi?

### Her gün yerine haftalık göndermek istersem?
```yaml
schedule:
  - cron: '0 5 * * 1'  # Her Pazartesi 08:00 TR
```

### Birden fazla kişiye göndermek istersem?
- Her kişi için ayrı CHAT_ID alın
- Bot kodunda loop ile hepsine gönderin

---

## ✅ Kontrol Listesi

- [ ] Bot oluşturdum (@BotFather)
- [ ] TOKEN aldım
- [ ] Karşı taraf botu aktif etti (/start)
- [ ] CHAT_ID öğrendim (getUpdates)
- [ ] GitHub Secrets ekledim
- [ ] Manuel test yaptım (Actions → Run workflow)
- [ ] Mesaj geldi ✅

---

🎉 **Tebrikler!** Sisteminiz hazır. Yarın sabah ilk otomatik mesajı alacaksınız.
