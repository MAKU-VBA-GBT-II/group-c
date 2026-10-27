# BE doğrulama kaydı — Issue #25

Tarih: 27 Ekim 2026. Kaynak: `data/banka-islemleri.csv`, geri yükleme tabanı `3ff108b`.

Komut: `python -m unittest discover -s tests -p test_csv_validation.py -v`

Testler gerçek CSV'nin geçici kopyaları üzerinde ayrı süreçlerde çalışır; kaynak CSV ve mevcut analiz raporu değiştirilmez.

| Kontrol | Gerçekleşen sonuç | Durum |
|---|---|---|
| Gerçek CSV ile analiz | 500 kayıt işlendi; ortalama 17.837,13 TL ve başarılı hacim 8.157.510,37 TL doğrulandı. Mevcut analiz hesapları korundu. | Geçti |
| Geçersiz takvim tarihi ve yanlış tarih biçimi | Her üç işlem durumunda da reddedildi; hata dosya, CSV satırı 2 ve tarih alanını gösterdi. | Geçti |
| Sayı yerine metin, NaN ve süre alanında ondalık değer | Tutar, müşteri kimliği ve süre hataları ilgili alan ve satır bilgisiyle reddedildi. | Geçti |
| Boş işlem türü | Her üç işlem durumunda da zorunlu değer hatası verildi. | Geçti |
| Hatalı veri ile raporun korunması | 21 hatalı veri denemesinin tamamında çıkış kodu sıfırdan farklı; mevcut rapor değişmedi. | Geçti |

Kanıt: skills/be-veri/SKILL.md becerisini kullanarak Codex ve Python unittest ile ürettim.
