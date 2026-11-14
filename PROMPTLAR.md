# Yapay zekâ çalışma günlüğü

Araç: OpenAI ChatGPT (GPT-6), 13 Kasım 2026.

**Şeffaflık notu:** Aşağıdaki maddeler bu konuşmada verilen ana talep ve bunun alt görevlere ayrılmasıyla oluşturulan *çalışma aşamalarını* açıklar. Kullanıcının ayrıca beş ayrı mesaj gönderdiği iddia edilmez. Gerçek kişisel kararlar ve sonradan yapılan düzeltmeler teslim öncesinde öğrenci tarafından doğrulanmalıdır.

| No | İstek / alt görev | Üretilen yaklaşım | Kabul / düzenleme ve gerekçe |
|---|---|---|---|
| 1 | Eczacıların tekrar eden bir sorununu belirle. | Stok ve son kullanma tarihi kontrolü. | Kabul: Somut ve ölçülebilir problem. |
| 2 | En az üç girdili ve doğrulamalı Python menüsü oluştur. | İlaç adı, stok, minimum stok, tarih; tekrar isteyen giriş fonksiyonları. | Kabul: Hatalı girişte program kapanmıyor. |
| 3 | Stok ve tarih için ayrı karar kuralları geliştir. | Geçmiş / 30 gün içinde / normal ve stok yok / kritik / yeterli. | Düzenleme: Sıfır stok kritik stoktan önce kontrol edildi. |
| 4 | Hatalı ve sınır değerli testler yaz. | Yedi otomatik test. | Kabul: Geçersiz sayı ve takvim dışı tarih denendi. |
| 5 | Rapor, CSV ve GitHub açıklamasını hazırla. | CSV yazımı, README ve rapor. | Düzenleme: Veri kalıcılığı sınırı açıklandı; CSV geri yükleme özelliği varmış gibi sunulmadı. |

## Yakalanan eksik/yanlış yaklaşım
İlk kural taslağında `stok <= minimum` kontrolü tek başına kullanılsaydı, stok sıfır olduğunda yalnızca `KRITIK STOK` yazacaktı. Bu, stok yokluğunu açıkça göstermeyeceği için eksikti. Önce `stok == 0` kontrolü eklendi. `test_stok_sifir` bu sınırı doğruluyor. Bu açıklama kod tasarımında ele alınan potansiyel hata örneğidir; gerçekleşmemiş bir test başarısızlığı olarak sunulmaz.

## Öğrenci doğrulaması
Öğrenci, kodu kendi bilgisayarında çalıştırmalı, ekran görüntülerini çekmeli, beyanı imzalamalı ve bu günlüğe kendi yaptığı gerçek değişiklikleri eklemelidir.
