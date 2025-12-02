# Instagram-Downloader

Instagram gönderilerini otomatik olarak indirmek için Python tabanlı bir araç.

## 📝 Açıklama

Bu proje, Instagram hesaplarından gönderileri otomatik olarak indirmek için Selenium ve yt-dlp kullanır. Belirtilen hesapların son gönderilerini bulup, video veya fotoğraf olarak bilgisayarınıza indirir.

## ✨ Özellikler

- 🔐 Otomatik Instagram girişi
- 📱 Instagram hesaplarından son gönderi indirme
- 🎥 Video ve fotoğraf desteği
- 🔗 Güvenli URL kopyalama ve işleme
- 🤖 Selenium ile tam otomatik işlem

## 🛠️ Gereksinimler

- Python 3.6 veya üzeri
- Google Chrome tarayıcısı
- İnternet bağlantısı
- Instagram hesabı

## 📦 Kurulum

### 1. Gerekli Python paketlerini yükleyin:

```bash
pip install selenium yt-dlp pyperclip
```

### 2. ChromeDriver kurulumu:

**Otomatik kurulum (önerilen):**
```bash
pip install webdriver-manager
```

**Manuel kurulum:**
1. Chrome tarayıcınızın sürümünü kontrol edin (chrome://version/)
2. [ChromeDriver](https://chromedriver.chromium.org/) sayfasından uygun sürümü indirin
3. İndirdiğiniz dosyayı sistem PATH'inize ekleyin

### 3. Projeyi klonlayın:

```bash
git clone https://github.com/kullaniciadi/Instagram-Downloader.git
cd Instagram-Downloader
```

## ⚙️ Yapılandırma

### Kullanıcı Bilgilerini Ayarlama

`index.py` dosyasında aşağıdaki satırları kendi bilgilerinizle güncelleyin:

```python
browser.find_element(By.NAME, 'username').send_keys("KULLANICI_ADINIZ")
browser.find_element(By.NAME, 'password').send_keys("ŞİFRENİZ")
```

### Hedef Hesabı Belirleme

İndirmek istediğiniz Instagram hesabını değiştirmek için:

```python
browser.get('https://www.instagram.com/HEDEF_HESAP_ADI/')
```

## 🚀 Kullanım

1. Gerekli ayarlamaları yaptıktan sonra scripti çalıştırın:

```bash
python index.py
```

2. Script otomatik olarak:
   - Instagram'a giriş yapacak
   - Belirtilen hesaba gidecek
   - Son gönderiyi bulacak
   - İndirme linkini kopyalayacak
   - Gönderiyi indirecek

## ⚠️ Önemli Uyarılar

### Güvenlik
- **Asla** kullanıcı adı ve şifrenizi kodda sabit olarak bırakmayın
- Çevre değişkenleri (environment variables) kullanmayı düşünün
- İki faktörlü kimlik doğrulamayı devre dışı bırakmanız gerekebilir

### Yasal Uyarılar
- Bu araç yalnızca eğitim amaçlıdır
- Instagram'ın Kullanım Şartları'na uygun kullanım yapın
- Telif hakkı korumalı içerikleri indirirken dikkatli olun
- Başkalarının gizliliğine saygı gösterin

### Teknik Notlar
- Instagram arayüzü değişikliklerinden etkilenebilir
- Çok sık kullanım hesap kısıtlamalarına yol açabilir
- Kararlı internet bağlantısı gereklidir

## 🔧 Sorun Giderme

### Yaygın Sorunlar

**ChromeDriver bulunamıyor hatası:**
```bash
pip install webdriver-manager
```
Ardından kod başında ekleyin:
```python
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
```

**Element bulunamıyor hatası:**
- Instagram arayüzü değişmiş olabilir
- Bekleme sürelerini artırmayı deneyin
- Element seçicilerini güncelleyin

**Giriş yapılamıyor:**
- Kullanıcı adı/şifre kontrolü yapın
- İki faktörlü kimlik doğrulamayı kontrol edin
- Instagram tarafından engellenmemiş olduğunuzdan emin olun

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyin.

## ⚖️ Sorumluluk Reddi

Bu araç yalnızca eğitim ve araştırma amaçlıdır. Kullanıcılar, bu aracı kullanırken tüm yasal sorumluluğu kabul eder. Geliştiriciler, aracın kötüye kullanımından kaynaklanan herhangi bir sorundan sorumlu değildir.

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**Not:** Instagram'ın API politikaları ve kullanım şartları sık sık değişir. Bu aracı kullanmadan önce güncel politikaları kontrol etmeniz önerilir.
