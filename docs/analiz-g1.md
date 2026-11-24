# G1 Veri Analizi Raporu

## 1. Veri setinin özeti

- Toplam kayıt: **500**
- Sütun sayısı: **15**
- Benzersiz işlem ID sayısı: **500**
- Başarılı işlem sayısı: **431**
- Başarılı işlemlerin toplam tutarı: **41,535,430.72 TL**

## 2. Metrikler ve yorumlar

### Metrik 1 — Toplam işlem sayısı

- Sonuç: **500 işlem**
- Yorum: Bu sayı, veri setindeki başarılı, başarısız ve beklemedeki tüm işlem kayıtlarını kapsar.

### Metrik 2 — Ortalama işlem tutarı

- Sonuç: **95,727.63 TL**
- Yorum: Ortalama, tüm kayıtların tutarları üzerinden hesaplanmıştır. Başarısız veya beklemedeki işlemler de bu metrikte yer alır.

### Metrik 3 — İşlem türlerine göre dağılım

- Döviz Satımı: **71 işlem** (%14.2)
- Havale: **70 işlem** (%14.0)
- Para Yatırma: **67 işlem** (%13.4)
- Para Çekme: **67 işlem** (%13.4)
- EFT: **66 işlem** (%13.2)
- Yurtdışı Para Transferi (SWIFT): **60 işlem** (%12.0)
- Döviz Alımı: **51 işlem** (%10.2)
- Kredi Kartı Borç Ödeme: **48 işlem** (%9.6)

- Yorum: Bu dağılım, hangi işlem türlerinin daha sık kullanıldığını gösterir; tek başına finansal hacmi göstermez.

### Metrik 4 — Müşteri segmentlerine göre dağılım

- Bireysel: **313 işlem** (%62.6)
- Ticari: **156 işlem** (%31.2)
- Kurumsal: **31 işlem** (%6.2)

- Yorum: Segment dağılımı, işlem kayıtlarının müşteri gruplarına göre nasıl dağıldığını gösterir. İşlem sayısı, benzersiz müşteri sayısı ile aynı değildir.

### Metrik 5 — Başarılı işlem hacminde ilk üç işlem türü

1. **Döviz Satımı** — 7,093,413.22 TL
2. **Havale** — 5,921,270.37 TL
3. **EFT** — 5,513,394.91 TL

- Yorum: Sıralama yalnızca başarılı işlemlerin tutar toplamına göre yapılmıştır. Başarısız ve beklemedeki işlemler finansal hacme dahil edilmemiştir.

### Ek metrik — Ortalama işlem süresi

- Sonuç: **207.70 saniye**
- Yorum: Bu değer tüm işlemlerin ortalama süresidir. Kanal ve işlem türüne göre ayrıca incelenmesi performans sorunlarını ortaya çıkarabilir.

## 3. Somut gözlemler

1. Veri setinde toplam **500 işlem** bulunmaktadır.
2. En sık görülen işlem türü **Döviz Satımı** olup 71 kayıt içerir.
3. En fazla işlem kaydı bulunan müşteri segmenti **Bireysel** segmentidir (313 kayıt).

## 4. Önerilen eylem

Başarısız ve beklemedeki işlemler kanal ve işlem türüne göre ayrıca incelenmelidir. Başarısızlık oranı belirli bir kanalda yükseliyorsa ilgili süreç araştırılmalı; işlem hacmi değerlendirmelerinde yalnızca başarılı işlemlerin tutarları kullanılmalıdır.

## 5. Veri kontrol notları

- Benzersiz işlem ID sayısı: 500 / 500
- Durum dağılımı: {'Başarılı': 431, 'Başarısız': 24, 'Şüpheli/Beklemede': 45}
- Bu rapor sentetik eğitim verisine dayanır; gerçek banka istatistiklerini temsil etmez.
