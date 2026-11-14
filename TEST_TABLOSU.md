# Test senaryoları (otomatik testler)

| No | Girdi | Beklenen | Gerçek | Sonuç |
|---|---|---|---|---|
| 1 | 20 stok, min 5, SKT 2030-12-31, bugün 2030-01-01 | NORMAL / YETERLI | NORMAL / YETERLI | Geçti |
| 2 | 5 stok, min 5, SKT bugün | 30 GUN ICINDE / KRITIK STOK | 30 GUN ICINDE / KRITIK STOK | Geçti |
| 3 | SKT dünden önce | SURESI DOLMUS | SURESI DOLMUS | Geçti |
| 4 | Stok 0, min 5 | STOK YOK | STOK YOK | Geçti |
| 5 | Stok girişi abc, -3, sonra 4 | İki uyarı, sonra 4 kabul | İki uyarı, 4 kabul | Geçti |
| 6 | Tarih 2030-02-30, sonra 2030-03-01 | Uyarı, geçerli tarihi kabul | Uyarı, tarihi kabul | Geçti |
| 7 | Boş ilaç adı, sonra Ornek Ilac | Uyarı, adı kabul | Uyarı, adı kabul | Geçti |

Test komutu: `python -m unittest -v`. Sonuç dosyası: `test_sonuclari.txt`.
