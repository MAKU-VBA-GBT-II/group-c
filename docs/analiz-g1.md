# G1 Veri Analizi Raporu

## 1. Veri setinin özeti

- Toplam kayıt: **500**
- Sütun sayısı: **10**
- Benzersiz işlem ID sayısı: **500**
- Başarılı işlem sayısı: **451**
- Başarılı işlemlerin toplam tutarı: **8.157.510,37 TL**

## 2. Metrikler ve yorumlar

### Metrik 1 — Toplam işlem sayısı

- Sonuç: **500 işlem**
- Yorum: Bu sayı, veri setindeki başarılı, başarısız ve beklemedeki tüm işlem kayıtlarını kapsar.

### Metrik 2 — Ortalama işlem tutarı

- Sonuç: **17.837,13 TL**
- Yorum: Ortalama, tüm kayıtların tutarları üzerinden hesaplanmıştır. Başarısız veya beklemedeki işlemler de bu metrikte yer alır.

### Metrik 3 — İşlem türlerine göre dağılım

- EFT: **72 işlem** (%14,4)
- Para yatırma: **72 işlem** (%14,4)
- Havale: **72 işlem** (%14,4)
- Kredi kartı borç ödeme: **71 işlem** (%14,2)
- Kredi taksiti ödeme: **71 işlem** (%14,2)
- Para çekme: **71 işlem** (%14,2)
- Fatura ödeme: **71 işlem** (%14,2)

**Yorum:** Bu dağılım, hangi işlem türlerinin daha sık kullanıldığını gösterir; tek başına finansal hacmi göstermez.

### Metrik 4 — Müşteri segmentlerine göre dağılım

- Bireysel: **329 işlem** (%65,8)
- Ticari: **152 işlem** (%30,4)
- Kurumsal: **19 işlem** (%3,8)

**Yorum:** Segment dağılımı, işlem kayıtlarının müşteri gruplarına göre nasıl dağıldığını gösterir. İşlem sayısı, benzersiz müşteri sayısı ile aynı değildir.

### Metrik 5 — Başarılı işlem hacminde ilk üç işlem türü

1. **Fatura ödeme** — 1.364.774,80 TL
2. **Kredi kartı borç ödeme** — 1.249.278,73 TL
3. **EFT** — 1.182.322,37 TL

**Yorum:** Sıralama yalnızca başarılı işlemlerin tutar toplamına göre yapılmıştır. Başarısız ve beklemedeki işlemler finansal hacme dahil edilmemiştir.

### Ek metrik — Ortalama işlem süresi

- Sonuç: **423,38 saniye**
- Yorum: Bu değer tüm işlemlerin ortalama süresidir. Kanal ve işlem türüne göre ayrıca incelenmesi performans sorunlarını ortaya çıkarabilir.

## 3. Somut gözlemler

1. Veri setinde toplam **500 işlem** bulunmaktadır.
2. **EFT, Para yatırma ve Havale** işlem türleri, 72'şer kayıtla en sık görülen işlem türleri arasında eşit olarak ilk sıradadır.
3. En fazla işlem kaydı bulunan müşteri segmenti **Bireysel** segmentidir (329 kayıt).

## 4. Önerilen eylem

Başarısız ve beklemedeki işlemler kanal ve işlem türüne göre ayrıca incelenmelidir. Başarısızlık oranı belirli bir kanalda yükseliyorsa ilgili süreç araştırılmalı; işlem hacmi değerlendirmelerinde yalnızca başarılı işlemlerin tutarları kullanılmalıdır.

## 5. Veri kontrol notları

- Benzersiz işlem ID sayısı: **500 / 500**
- Durum dağılımı: Başarılı **451**, Başarısız **36**, Beklemede **13**
- Bu rapor sentetik eğitim verisine dayanır; gerçek banka istatistiklerini temsil etmez.