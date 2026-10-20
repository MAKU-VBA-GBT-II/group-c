# DQ Test — Test Senaryoları

## Amaç
Banka işlemleri veri hattındaki veri dosyasının yapısını, veri kalitesini ve analiz çıktısını kontrol etmek.

## Test 1 — CSV dosyasının varlığı
- **Kontrol:** `data/banka-islemleri.csv` dosyası mevcut mu?
- **Beklenen sonuç:** Dosya bulunmalı ve okunabilmeli.
- **Durum:** Henüz test edilmedi.

## Test 2 — Satır sayısı
- **Kontrol:** CSV dosyasında başlık satırı dışında 500 kayıt var mı?
- **Beklenen sonuç:** Toplam 500 veri kaydı bulunmalı.
- **Durum:** Henüz test edilmedi.

## Test 3 — Sütun adları
- **Kontrol:** Dosyada beklenen 10 sütun bulunuyor mu?
- **Beklenen sütunlar:** `islem_id`, `tarih`, `musteri_id`, `islem_turu`, `tutar`, `kanal`, `sehir`, `durum`, `musteri_segmenti`, `islem_suresi_sn`.
- **Beklenen sonuç:** Sütun adları ve sıraları doğru olmalı.
- **Durum:** Henüz test edilmedi.

## Test 4 — Veri türleri ve boş değerler
- **Kontrol:** `islem_id` ve `musteri_id` alanları kimlik değerleri içermeli; `tarih` geçerli bir tarih olmalı; `tutar` sayısal, `islem_suresi_sn` tam sayı olmalı. Zorunlu alanlar boş olmamalı.
- **Beklenen sonuç:** Değerler uygun türde olmalı ve zorunlu alanlarda boşluk bulunmamalı.
- **Durum:** Henüz test edilmedi.

## Test 5 — Kategori değerleri
- **Kontrol:** `islem_turu`, `kanal`, `sehir`, `durum` ve `musteri_segmenti` alanlarındaki kategoriler veri sözlüğündeki değerlerle uyumlu mu?
- **Beklenen sonuç:** Tanımsız veya beklenmeyen kategori değerleri bulunmamalı.
- **Durum:** Henüz test edilmedi.

## Test 6 — İşlem kimliklerinin benzersizliği
- **Kontrol:** `islem_id` değerleri tekrarlanıyor mu?
- **Beklenen sonuç:** Her işlem kimliği benzersiz olmalı.
- **Durum:** Henüz test edilmedi.

## Test 7 — Analiz raporunun varlığı
- **Kontrol:** `docs/analiz-g1.md` dosyası mevcut mu ve temel analiz sonuçlarını içeriyor mu?
- **Beklenen sonuç:** Rapor bulunmalı; toplam işlem sayısı, ortalama tutar ve başarılı işlem hacmi gibi temel sonuçlar yer almalı.
- **Durum:** Henüz test edilmedi.

## Genel değerlendirme
Testler çalıştırıldıktan sonra her senaryonun gerçek sonucu kaydedilmeli ve durumu **Başarılı** veya **Başarısız** olarak güncellenmelidir.
