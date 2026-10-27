# DQ Test Skill'i

## 1. Amaç
Bu beceri, banka işlemleri veri hattının girdilerini ve analiz çıktısını kontrol etmek için test senaryoları hazırlar. Senaryolar `tests/test-cases.md` dosyasında tutulur.

## 2. Adım Adım Talimatlar
1. Depo kök dizininde çalıştığını kontrol et.
2. `data/banka-islemleri.csv` dosyasının mevcut olduğunu kontrol et.
3. `docs/veri-sozlugu-g1.md` dosyasını inceleyerek sütunları, veri türlerini ve izin verilen kategori değerlerini belirle.
4. `src/dq_analiz.py` betiğini inceleyerek analiz girdilerini ve çıktısını belirle.
5. `tests/test-cases.md` dosyasını oluştur veya mevcut senaryoları güncelle.
6. Her test için benzersiz bir ID, adımlar, girdi ve beklenen sonucu yaz.
7. En az beş test senaryosu tanımla.
8. Satır sayısı, sütunlar, veri türleri ve kategori değerlerini kapsayan senaryolar ekle.
9. İşlem kimliklerinin benzersizliğini ve analiz raporunun varlığını da kontrol kapsamına al.
10. Senaryoların anlaşılır, tekrarlanabilir ve veri sözlüğüyle uyumlu olduğunu kontrol et.

## 3. Kullanılan Dosyalar
- Test senaryoları: `tests/test-cases.md`
- Girdi verisi: `data/banka-islemleri.csv`
- Veri sözlüğü: `docs/veri-sozlugu-g1.md`
- Analiz betiği: `src/dq_analiz.py`
- Analiz raporu: `docs/analiz-g1.md`

## 4. Test Senaryosu Şablonu
Her senaryo aşağıdaki alanları içermelidir:
- **ID:** Testin benzersiz numarası.
- **Adımlar:** Testin nasıl uygulanacağı.
- **Girdi:** Testte kullanılacak dosya, alan veya örnek değer.
- **Beklenen:** Test başarılı olduğunda beklenen sonuç.

## 5. Çalışma Talimatları
Depo kök dizininde test senaryolarını düzenlemek için:

`notepad tests\test-cases.md`

Analiz betiğini çalıştırmak için:

`python src/dq_analiz.py`

Bu komut analiz raporunu üretir. Test senaryolarının hazırlanması ile testlerin fiilen çalıştırılması farklı işlemlerdir; yalnızca senaryo hazırlama görevi verildiyse testlerin çalıştırıldığı iddia edilmemelidir.

## 6. Kabul Kriterleri
- `tests/test-cases.md` dosyası mevcut olmalıdır.
- En az beş test senaryosu tanımlanmalıdır.
- Satır sayısı, sütunlar, veri türleri ve kategori bilgileri kapsanmalıdır.
- Her senaryoda ID, Adımlar, Girdi ve Beklenen alanları bulunmalıdır.
- Senaryolar açık, tutarlı ve tekrarlanabilir olmalıdır.

## 7. Test Sonuçlarının Kaydedilmesi

1. Testleri uygulamadan önce `tests/test-cases.md` dosyasındaki senaryoları incele.
2. Her senaryoyu ilgili veri ve dosyalar üzerinde çalıştır. Gerçekleştirilmemiş testleri başarılı olarak işaretleme.
3. Test sonuçlarını `tests/test-log.md` dosyasına tarihli olarak kaydet. Dosya mevcut değilse oluştur.
4. Her test kaydında şu alanları kullan:
   - **Tarih:** `YYYY-MM-DD` biçiminde test tarihi.
   - **Test ID / Adı:** Uygulanan senaryonun kimliği ve adı.
   - **Beklenen Sonuç:** Senaryoda tanımlanan sonuç.
   - **Gerçekleşen Sonuç:** Test sırasında gözlenen sonuç.
   - **Durum:** Başarılı veya Başarısız.
   - **Notlar:** Hata, sapma veya ek açıklamalar.
5. Yeni kayıtları mevcut kayıtların sonuna ekle; önceki test sonuçlarını silme veya üzerine yazma.
6. Test başarısız olursa beklenen ve gerçekleşen sonuç arasındaki farkı açıkça belirt.

### Test Kaydı Şablonu

| Tarih | Test ID / Adı | Beklenen Sonuç | Gerçekleşen Sonuç | Durum | Notlar |
|---|---|---|---|---|---|
| YYYY-MM-DD | T01 - Örnek test | Beklenen sonuç | Gözlenen sonuç | Başarılı/Başarısız | Açıklama |

### Ek Kabul Kriterleri

- `tests/test-log.md` dosyası test sonuçlarını kaydetmek için kullanılmalıdır.
- Her gerçekleştirilen test tarih ve sonuç bilgisi içermelidir.
- Test kayıtları geçmiş sonuçları koruyacak şekilde eklenmelidir.
- Çalıştırılmayan testler için başarı sonucu yazılmamalıdır.