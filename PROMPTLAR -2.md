# GEP1316 – ECZANE İLAÇ STOK VE SON KULLANMA TARİHİ TAKİP SİSTEMİ
## Gerçek Yapay Zekâ Promptlari
**Öğrenci:** Ezgi Vural
**Kullanılan araç:** OpenAI ChatGPT


## Prompt 1 – Fonksiyonların Görevleri
**Gönderilen soru:**
Eczane ilaç stok takip projemde kullandığım `pozitif_tamsayi_oku`, `tarih_oku` ve `durum_hesapla` fonksiyonlarının görevlerini ve neden ayrı fonksiyonlar olarak yazıldıklarını açıklar mısın?
**Yanıt özeti:** Sayı ve tarih doğrulama ile stok/SKT durum hesaplaması açıklandı. Ayrı fonksiyonların tekrar kullanım, okunabilirlik ve test kolaylığı sağladığı belirtildi.

## Prompt 2 – Hatalı Girişlerin Yönetimi
**Gönderilen soru:**
Eczane ilaç stok takip projemde kullanıcı yanlışlıkla negatif stok miktarı, harf içeren sayı veya geçersiz son kullanma tarihi girerse program nasıl tepki veriyor? Bu hataları önlemek için kullanılan `try-except` ve `while` yapılarının görevlerini örneklerle açıklar mısın?
**Yanıt özeti:** Negatif stok, sayıya çevrilemeyen giriş ve geçersiz tarih için uyarı ve yeniden giriş davranışı; try-except, while, continue ve break yapıları örneklerle açıklandı.

## Prompt 3 – Karar Kuralları
**Gönderilen soru:**
Eczane ilaç stok takip projemde durum_hesapla() fonksiyonu ilaçların stok durumunu ve son kullanma tarihini nasıl değerlendiriyor? if-elif-else yapısının görevini açıklayarak STOK YOK, KRITIK STOK, SURESI DOLMUS ve 30 GUN ICINDE sonuçlarının hangi koşullarda oluştuğunu örneklerle anlatır mısın?
**Yanıt özeti:** Stok sıfırsa STOK YOK; sıfırdan büyük ve minimuma eşit/altındaysa KRITIK STOK. SKT geçmişse SURESI DOLMUS; bugün ile 30 gün arasındaysa 30 GUN ICINDE. Koşul sıralamasının önemi açıklandı.

## Prompt 4 – Otomatik Testler
**Gönderilen soru:**
Eczane ilaç stok takip projemde test_eczane.py dosyasında bulunan 7 otomatik testin her biri neyi kontrol ediyor? unittest kütüphanesinin görevini, testlerin neden önemli olduğunu ve test sonuçlarında görülen Ran 7 tests ile OK ifadelerinin anlamlarını açıklar mısın?
**Yanıt özeti:** Yedi senaryo (normal, son gün, süresi dolmuş, stok sıfır, hatalı sayı, hatalı tarih, boş ad) ve unittest kütüphanesi açıklandı. Ran 7 tests yedi testin çalıştığını, OK ise tamamının başarılı olduğunu gösterir.

## Prompt 5 – Csv Raporlama Ve Geliştirme
**Gönderilen soru:**
Eczane ilaç stok takip projemde CSV raporu nasıl oluşturuluyor? Python'daki csv kütüphanesinin görevini açıklar mısın? Oluşturduğum CSV dosyasını Excel'de açtığımda verilerin tek sütunda görünmesinin nedenini ve çözümünü anlatır mısın? Ayrıca programı gelecekte geliştirmek için hangi özellikleri ekleyebilirim?
**Yanıt özeti:** CSV dışa aktarımı ve csv modülü açıklandı. Excel'in beklediği ayırıcı ile dosyanın ayırıcısı farklı olduğunda verilerin tek sütunda görünebileceği; Veri > Metinden/CSV'den veya Metni Sütunlara Dönüştür seçenekleriyle düzeltilebileceği belirtildi. Veri geri yükleme, arama, güncelleme ve veritabanı önerildi.

