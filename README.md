# Eczane İlaç Stok ve Son Kullanma Tarihi Takip Sistemi

**Ders:** GEP1316 – Kodlama Okuryazarlığı  
**Öğrenci:** Ezgi Vural  
**Proje türü:** Python komut satırı uygulaması

## Projenin amacı

Eczanelerde ilaçların stok miktarlarını ve son kullanma tarihlerini takip etmek önemlidir. Bu mini uygulama, girilen ilaç bilgilerine göre stok ve tarih durumunu hesaplar, ekranda rapor gösterir ve sonuçları CSV dosyasına kaydeder. Eğitim amaçlı hazırlanmıştır; gerçek hasta verisi içermez ve ilaç kullanımına ilişkin profesyonel karar vermez.

## Nasıl çalıştırılır?

Bilgisayarda **Python 3.9 veya üzeri** bulunmalıdır. `eczane.py` dosyasının bulunduğu klasörde terminal açılarak şu komut çalıştırılır:

```bash
python eczane.py
```

Program menüsü:

1. **İlaç ekle:** İlaç adı, stok adedi, minimum stok adedi ve son kullanma tarihi girilir.
2. **Rapor göster:** Kayıtlı ilaçların stok ve tarih durumları görüntülenir.
3. **CSV kaydet:** `eczane_raporu.csv` dosyası oluşturulur.
4. **Çıkış:** Program sonlandırılır.

Son kullanma tarihi `YYYY-AA-GG` biçiminde girilmelidir (örnek: `2027-06-15`). Kayıtlar program çalışırken bellekte tutulur; program yeniden açıldığında eski kayıtlar otomatik yüklenmez.

## Kontrol kuralları

| Kontrol | Programın gösterdiği durum |
|---|---|
| Son kullanma tarihi geçmiş | `SURESI DOLMUS` |
| Son kullanma tarihine 0–30 gün kalmış | `30 GUN ICINDE` |
| Son kullanma tarihine 30 günden fazla kalmış | `NORMAL` |
| Stok adedi 0 | `STOK YOK` |
| Stok adedi 0'dan büyük, minimuma eşit veya altında | `KRITIK STOK` |
| Stok adedi minimumun üzerinde | `YETERLI` |

Boş ilaç adı, harf içeren stok miktarı, negatif stok miktarı ve geçersiz tarih girişlerinde program uyarı vererek yeniden giriş ister. **Sıfır stok geçerlidir** ve `STOK YOK` olarak raporlanır.

## Bilgisayarda yapılan testler

Aşağıdaki testler Python terminalinde elle uygulanmış ve sonuçları kontrol edilmiştir:

| Test | Girilen değer | Gözlenen sonuç |
|---|---|---|
| 1. Sayı yerine harf | `abc` | `Uyari: Lutfen tam sayi giriniz.` |
| 2. Negatif stok | `-5` | `Uyari: Gecerli bir pozitif sayi giriniz.` |
| 3. Geçersiz tarih | `2027-15-40` | Tarih biçimi uyarısı; yeniden giriş istendi |
| 4. Tarihi geçmiş ilaç | Majezik, `2025-01-15` | `SURESI DOLMUS` |
| 5. Sıfır stok | Vermidon, `0` | `STOK YOK` |

Ayrıntılı test notları `TEST_TABLOSU.md` dosyasında yer alır.

## Ekran görüntüleri

- [Programın ana menüsü](ekran_goruntuleri/01_ana_menu.jpg)
- [Hatalı stok girişi](ekran_goruntuleri/02_hatali_stok.jpg)
- [Geçersiz tarih ve tarihi geçmiş ilaç raporu](ekran_goruntuleri/03_gecersiz_tarih.jpg)
- [Sıfır stok raporu](ekran_goruntuleri/04_sifir_stok.jpg)
- [CSV dosyasının Excel'de açılması](ekran_goruntuleri/05_csv_excel.jpg)

*Not:* CSV dosyası Excel'de ilk açıldığında virgülle ayrılmış alanlar tek sütunda görünebilir. Excel'de **Veri > Metni Sütunlara Dönüştür > Virgül** seçilerek ayrı sütunlarda görüntülenebilir.

## Proje dosyaları

| Dosya / klasör | İçeriği |
|---|---|
| `eczane.py` | Ana Python uygulaması |
| `README.md` | Proje tanıtımı ve kullanım kılavuzu |
| `PROMPTLAR.md` | Yapay zekâ kullanım ve değerlendirme günlüğü |
| `TEST_TABLOSU.md` | Manuel test senaryoları |
| `eczane_raporu_ORNEK.csv` | Örnek CSV çıktı dosyası |
| `ekran_goruntuleri/` | Gerçek uygulama ekran görüntüleri |

## Yapay zekâ kullanımı

Proje fikrinin geliştirilmesi, kod ve doküman taslaklarının hazırlanmasında ChatGPT desteğinden yararlanılmıştır. Programın çalıştırılması, girişlerin denenmesi ve ekrandaki sonuçların kontrolü bilgisayarda gerçekleştirilmiştir. Kullanım sürecinin ayrıntıları ve doğrulanması gereken prompt kayıtları `PROMPTLAR.md` dosyasındadır.
