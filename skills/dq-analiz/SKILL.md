---
name: dq-analiz
description: "Banka işlemleri sentetik veri setini analiz eder, temel metrikleri hesaplar ve docs/analiz-g1.md raporunu üretir."
---

# DQ Analiz Skill'i

## 1. Amaç
Bu beceri, banka işlemleri için oluşturulan sentetik CSV verisini analiz eder, temel metrikleri hesaplar ve sonuçları `docs/analiz-g1.md` dosyasına raporlar.

## 2. Adım Adım Talimatlar
1. `data/banka-islemleri.csv` dosyasının varlığını kontrol et.
2. `docs/veri-sozlugu-g1.md` dosyasından sütun adlarını ve anlamlarını öğren.
3. CSV dosyasını Python ile oku ve sütunların veri tiplerini kontrol et.
4. Toplam işlem sayısını hesapla.
5. Ortalama işlem tutarını hesapla.
6. En az iki kategorik alana göre kırılım analizi yap.
7. Belirlediğin ölçüte göre ilk üç kaydı listele.
8. Her metrik için 1–2 cümlelik yorum yaz.
9. Analiz sonuçlarından üç somut gözlem çıkar.
10. Veriye dayalı en az bir eylem önerisi oluştur.
11. Sonuçları `docs/analiz-g1.md` dosyasına kaydet.
12. Hesaplamaları gerçek veriden doğrula; tahmini değerleri gerçek sonuç gibi gösterme.

## 3. Kullanılan Dosyalar
- Girdi verisi: `data/banka-islemleri.csv`
- Veri sözlüğü: `docs/veri-sozlugu-g1.md`
- Analiz raporu: `docs/analiz-g1.md`

## 4. Çalıştırma Talimatları

### Ön koşullar
- Python 3 kurulu olmalıdır.
- Betik yalnızca Python standart kütüphanesini kullanır: `csv`, `math`, `sys`, `collections`, `datetime`, `pathlib` ve `statistics`.
- `pandas` veya başka bir harici Python paketi kurulması gerekmez.
- Komutlar depo kök dizininde çalıştırılmalıdır.

### Çalıştırma
1. Komut satırında depo kök dizinine git.
2. Python sürümünü kontrol et: `python --version`
3. Analiz betiğini çalıştır: `python src/dq_analiz.py`
4. İşlem başarılıysa `docs/analiz-g1.md` dosyasının oluşturulduğunu veya güncellendiğini kontrol et.
5. Betik hata verirse hata mesajını incele; hata giderilmeden analiz başarılı olarak raporlanmamalıdır.
