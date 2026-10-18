---
name: be-veri
description: Bankacılık sektörü için sentetik işlem verisi üretir ve doğrular.
---

# BE — Bankacılık Veri Üretimi

## 1. Amaç

Bu beceri, bankacılık sektörüne uygun sentetik işlem verileri üretmek için kullanılır. Sabit rastgelelik tohumu sayesinde veriler tekrar üretilebilir ve DQ ile FE ekiplerinin kullanımına hazır hale getirilir.

## 2. Veri Seti

- **Sektör:** Bankacılık
- **Kayıt sayısı:** 500
- **Sütun sayısı:** 10
- **Ana kategori:** İşlem türü (7 farklı değer)
- **Rastgelelik tohumu:** 42
- **Çıktı:** CSV

**Sütunlar:**

`islem_id`, `tarih`, `musteri_id`, `islem_turu`, `tutar`, `kanal`, `sehir`, `durum`, `musteri_segmenti`, `islem_suresi_sn`

**İşlem türleri:**

Havale, EFT, Para yatırma, Para çekme, Fatura ödeme, Kredi taksiti ödeme, Kredi kartı borç ödeme.

## 3. Ajanın İzleyeceği Adımlar

1. `docs/veri-sozlugu-g1.md` dosyasındaki DQ tarafından onaylanan veri şemasını incele.
2. `src/banka_veri_uret.py` dosyasında Python ile sentetik banka işlemleri üret.
3. Rastgele veri üretiminde `seed=42` kullan.
4. İşlem tutarlarını, tarihleri, kanalları ve süreleri mantıklı aralıklarda oluştur.
5. Verileri `data/banka-islemleri.csv` dosyasına UTF-8 formatında kaydet.
6. Dosyanın 500 satır, 10 sütun ve 7 işlem türü içerdiğini doğrula.
7. Eksik değerleri, işlem numaralarının benzersizliğini ve veri tiplerini kontrol et.
8. Aynı kod tekrar çalıştırıldığında aynı verilerin üretildiğini doğrula.
9. Hataları düzelt ve doğrulama sonuçlarını bildir.

## 4. Dosyalar ve Çalıştırma

| Dosya | Görevi |
|---|---|
| `src/banka_veri_uret.py` | Python veri üretim kodu |
| `data/banka-islemleri.csv` | Üretilen sentetik veriler |
| `docs/veri-sozlugu-g1.md` | Sütun açıklamaları ve veri kuralları |
| `skills/be-veri/SKILL.md` | Yapay zekâ ajanının talimatları |

**PowerShell üzerinden çalıştırma:**

`python src/banka_veri_uret.py`

## 5. Devir Teslim

Veri üretimi ve kontroller tamamlandıktan sonra dosyaları GitHub'a gönder.

Commit hash değerini alarak `G1-analiz` ve `G1-gorsel` issue'larına şu formatta yorum yaz:

**Veri hazır — commit `<hash>`.** 500 satırlık, 10 sütunlu sentetik bankacılık veri seti oluşturuldu. Veri sözlüğü ve üretim kodu repoya eklendi.