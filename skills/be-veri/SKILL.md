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
2. Mevcut `src/banka_veri_uret.py` betiğini kullan; yalnızca veri kuralları değişecekse betiği düzenle. Aynı betik ve Python sürümüyle tekrar üretim yap.
3. Rastgele veri üretiminde `seed=42` kullan.
4. Tarih, tutar, kanal ve süre kurallarını veri sözlüğü ve mevcut betikteki sınırlarla uygula; yeni aralıklar uydurma. Şema ile betik çelişiyorsa bunu raporla.
5. Verileri `data/banka-islemleri.csv` dosyasına UTF-8 (BOM'lu, utf-8-sig) formatında kaydet.
6. Dosyanın başlık hariç 500 veri kaydı (başlıkla 501 CSV satırı), 10 sütun ve 7 işlem türü içerdiğini doğrula.
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

Depo kök dizininde Python 3 kullan. Betik yalnızca standart kütüphaneyi kullanır; ek paket kurulumu gerekmez.

`python src/banka_veri_uret.py`

Komut mevcut `data/banka-islemleri.csv` dosyasının üzerine yazar. Veri sözlüğünü ve DQ/FE raporlarını değiştirme. Yeniden üretim kontrolünü geçici bir dizinde betiğin kopyasını iki ayrı süreçte çalıştırıp oluşan CSV dosyalarının SHA-256 değerlerini karşılaştırarak yap. Çıkış kodu sıfır değilse veya doğrulama başarısızsa teslimi başarılı olarak bildirme.

## 5. Devir Teslim

Veri üretimi ve kontroller tamamlandıktan sonra dosyaları GitHub'a gönder.

Commit hash değerini alarak `G1-analiz` ve `G1-gorsel` issue'larına şu formatta yorum yaz:

**Veri hazır — commit `<hash>`.** 500 satırlık, 10 sütunlu sentetik bankacılık veri seti oluşturuldu. Veri sözlüğü ve üretim kodu repoya eklendi.

Teslim yorumuna gerçekten kullanılan araçla şu satırı ekle (Codex örneği):

Kanıt: skills/be-veri/SKILL.md becerisini kullanarak Codex ile ürettim.
