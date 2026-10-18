# G1 — Bankacılık Sentetik Veri Sözlüğü

## 1. Veri Setinin Amacı

Bu veri seti, bankacılık sektöründeki müşteri işlemlerini simüle etmek amacıyla oluşturulacaktır. Veriler tamamen sentetik olup gerçek müşteri veya banka kayıtları içermeyecektir.

Veri seti, DQ ekibinin işlem analizlerini ve FE ekibinin görselleştirme çalışmalarını destekleyecektir.

## 2. Veri Setinin Genel Özellikleri

| Özellik | Değer |
|---|---|
| Sektör | Bankacılık |
| Veri konusu | Müşteri işlem kayıtları |
| Kayıt sayısı | 500 |
| Sütun sayısı | 10 |
| Ana kategorik değişken | `islem_turu` |
| İşlem türü sayısı | 7 |
| Rastgelelik tohumu | 42 |
| Para birimi | Türk lirası (TL) |
| Tarih aralığı | 01.01.2026 – 30.09.2026 |
| Dosya formatı | CSV (UTF-8) |

## 3. Veri Alanları

| Sütun | Veri tipi | Açıklama | Değer / Kural |
|---|---|---|---|
| `islem_id` | int | Benzersiz işlem numarası | 1001–1500 |
| `tarih` | date | İşlemin tarihi | YYYY-MM-DD |
| `musteri_id` | int | Sentetik müşteri numarası | 10001–10100 |
| `islem_turu` | string | Bankacılık işlem türü | 7 kategori |
| `tutar` | float | İşlem tutarı | 10–100.000 TL |
| `kanal` | string | İşlemin yapıldığı kanal | 4 kategori |
| `sehir` | string | İşlemin gerçekleştiği şehir | 6 kategori |
| `durum` | string | İşlemin sonucu | 3 kategori |
| `musteri_segmenti` | string | Müşteri grubu | 3 kategori |
| `islem_suresi_sn` | int | İşlem süresi | 5–1800 saniye |

## 4. Kategorik Değerler

**İşlem türleri (7):** Havale, EFT, Para yatırma, Para çekme, Fatura ödeme, Kredi taksiti ödeme, Kredi kartı borç ödeme.

**İşlem kanalları (4):** Mobil bankacılık, İnternet bankacılığı, ATM, Şube.

**Şehirler (6):** İstanbul, Ankara, İzmir, Antalya, Bursa, Burdur.

**İşlem durumları (3):** Başarılı, Başarısız, Beklemede.

**Müşteri segmentleri (3):** Bireysel, Ticari, Kurumsal.

## 5. Veri Üretim Kuralları

1. Python veri üretiminde `seed=42` kullanılacaktır.
2. Her işlem benzersiz bir `islem_id` değerine sahip olacaktır.
3. Aynı müşteri birden fazla işlem yapabilecektir.
4. İşlem tutarları pozitif ve iki ondalık basamaklı olacaktır.
5. Tarihler belirtilen aralıkta üretilecektir.
6. İşlem türleri ile kanallar arasında mantıksal uyum sağlanacaktır.
7. İşlem süreleri kullanılan kanala göre farklılık gösterebilecektir.
8. Zorunlu alanlarda eksik değer bulunmayacaktır.
9. Kategorik alanlarda tanımlanan değerlerin dışına çıkılmayacaktır.
10. Aynı kod ve seed kullanıldığında aynı veri seti üretilecektir.

Bu kurallar eğitim amaçlı sentetik varsayımlardır; gerçek banka istatistikleri olarak yorumlanmamalıdır.

## 6. Analiz ve Görselleştirme Kuralları

DQ ekibi toplam işlem sayısı, ortalama işlem tutarı, işlem türü dağılımı, müşteri segmenti dağılımı ve en yüksek işlem hacmine sahip ilk üç kategoriyi analiz edebilir.

Finansal işlem hacmi hesaplanırken yalnızca `durum = Başarılı` olan kayıtların tutarları toplanacaktır. Başarısız ve beklemede işlemler işlem sayısı analizlerine dahil edilebilir.

FE ekibi `tarih` alanını zaman serisi grafiği, `islem_turu` alanını ise kategorik dağılım grafiği için kullanabilir.

## 7. Dosya Bilgileri

**Veri üretim kodu:** `src/banka_veri_uret.py`

**Üretilen veri:** `data/banka-islemleri.csv`

**Yapay zekâ becerisi:** `skills/be-veri/SKILL.md`

**Çalıştırma komutu:** `python src/banka_veri_uret.py`