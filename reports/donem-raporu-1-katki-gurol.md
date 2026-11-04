# Dönem Raporu 1 – DQ Katkısı

**Ad Soyad:** Gürol Pekmezci  
**Rol:** DQ (Data Quality)  
**Takım:** Group C

## 1. Ne Teslim Ettim?

- Banka işlemleri veri setinin kalite analizini gerçekleştirdim.
- `src/dq_analiz.py` dosyasını oluşturdum.
- `docs/analiz-g1.md` analiz raporunu hazırladım.
- `tests/test-cases.md` dosyasında test senaryolarını oluşturdum.
- `tests/test-log.md` dosyasında test sonuçlarını belgeledim.
- DQ analiz ve test becerileri üzerinde çalıştım.

## 2. Neye Takıldım, Nasıl Aştım?

Git işlemleri sırasında uzak depodaki güncellemeler nedeniyle push ve rebase sorunları yaşadım. Uzak depodaki değişiklikleri alıp kendi çalışmalarımı güncelleyerek bu sorunları çözdüm.

## 3. Bir Sonraki Dönem İçin Önerim

Veri kalitesi kontrollerinin veri üretim aşamasından itibaren yapılmasını öneriyorum. Ayrıca BE ve DQ ekipleri arasındaki veri paylaşımının düzenli olması ve testlerin otomatikleştirilmesi faydalı olacaktır.

## 4. Test Sonucu

04.11.2026 tarihinde `python -m unittest discover -s tests -p test_csv_validation.py -v` komutuyla CSV doğrulama testlerini çalıştırdım.

- `test_invalid_values_preserve_report`: Başarılı
- `test_real_csv_succeeds`: Başarılı
- Toplam 2 test başarılı, 0 test başarısız.