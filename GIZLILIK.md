# 🔐 Gizli Bilgileri Koruma Rehberi

Bu proje hem **lokal testler** hem de **GitHub Actions** ile çalışır. Her ikisinde de gizli bilgileriniz (token, chat_id, mesaj) güvenli şekilde saklanır.

---

## 📋 Ne Nerede Saklanıyor?

| Bilgi | Lokal Test | GitHub Actions |
|-------|------------|----------------|
| Token | `.env` dosyası | GitHub Secrets |
| Chat ID | `.env` dosyası | GitHub Secrets |
| Mesaj | `.env` dosyası | GitHub Secrets |

---

## 🏠 1. Lokal Test (Bilgisayarınızda)

### Adım 1: .env dosyası oluştur

```bash
cp .env.example .env
```

### Adım 2: .env dosyasını düzenle

`.env` dosyasını açın ve kendi bilgilerinizi yazın:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
TELEGRAM_MESSAGE=🌅 Günaydın kuçuk bebeğim!

📅 Tarih: {today}

Seni çok seviyorum! 💕
```

**ÖNEMLİ:**
- `.env` dosyası `.gitignore` içinde → GitHub'a **GİTMEZ** ✅
- Mesajınızı istediğiniz gibi yazabilirsiniz
- `{today}` yazarsanız otomatik tarih eklenir

### Adım 3: Test et

```bash
# Gereksinimleri yükle
pip install -r requirements.txt

# Testi çalıştır
python test_local.py
```

---

## ☁️ 2. GitHub Actions (Otomasyon)

### Adım 1: GitHub Secrets'a ekle

1. Repo sayfası → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret** tıkla
3. Şu 3 secret'ı ekle:

#### Secret 1: TELEGRAM_BOT_TOKEN
```
Name: TELEGRAM_BOT_TOKEN
Secret: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

#### Secret 2: TELEGRAM_CHAT_ID
```
Name: TELEGRAM_CHAT_ID
Secret: 123456789
```

#### Secret 3: TELEGRAM_MESSAGE (YENİ!)
```
Name: TELEGRAM_MESSAGE
Secret: 🌅 Günaydın kuçuk bebeğim!

📅 Tarih: {today}

Seni çok seviyorum! 💕
```

**ÖNEMLİ:**
- GitHub Secrets **şifrelenmiş** saklanır ✅
- Repo public olsa bile **kimse göremez** ✅
- Actions loglarında **gizlenir** (*** ile gösterilir) ✅

### Adım 2: Test et

1. **Actions** sekmesine git
2. **Daily Telegram Message** → **Run workflow**
3. Mesajın geldiğini kontrol et

---

## 🔒 Güvenlik Kontrol Listesi

- [x] `.env` dosyası `.gitignore` içinde
- [x] Token'lar kodda hard-coded değil
- [x] Mesaj kodda hard-coded değil
- [x] GitHub Secrets kullanılıyor
- [x] Public repo'da gizli bilgi yok

---

## ❓ Sık Sorulan Sorular

### .env dosyam GitHub'a gider mi?
**HAYIR!** `.gitignore` içinde olduğu için git tarafından görmezden gelinir.

### Birisi repo'mu klonlarsa mesajımı görür mü?
**HAYIR!** Sadece `.env.example` görecek (örnek değerlerle). Asıl `.env` dosyanız lokaldir.

### GitHub Actions loglarında mesajım görünür mü?
GitHub Secrets kullandığınız için `***` ile gizlenir.

### Mesajımı nasıl değiştiririm?

**Lokal test için:**
- `.env` dosyasını düzenle

**GitHub Actions için:**
- Settings → Secrets → TELEGRAM_MESSAGE → Update

### Token'ımı değiştirmem gerekirse?

**Lokal:**
1. `.env` dosyasını güncelle

**GitHub:**
1. BotFather'dan yeni token al (eğer gerekiyorsa)
2. Settings → Secrets → TELEGRAM_BOT_TOKEN → Update

---

## 🧪 Test Komutları

```bash
# Lokal test
python test_local.py

# .env dosyasını kontrol et
cat .env  # (dikkat: gizli bilgiler içerir!)

# .gitignore kontrolü
git status  # .env görünmemeli
```

---

## ⚠️ DİKKAT!

**ASLA YAPMAYIN:**
- ❌ Token'ı kodda yazmayın
- ❌ `.env` dosyasını commit etmeyin
- ❌ Mesajı kodda hard-code etmeyin
- ❌ Secrets'ları screenshot'layıp paylaşmayın

**HER ZAMAN YAPIN:**
- ✅ `.env` kullanın (lokal)
- ✅ GitHub Secrets kullanın (Actions)
- ✅ `.gitignore` kontrol edin
- ✅ `.env.example` güncel tutun (değerler olmadan)

---

🎉 **Artık tüm gizli bilgileriniz güvende!**
