# Çok Ajanlı Şirket Programı: Öneri ve Roller

**Şirket:** VBA BANKACILIK (Grup C)  
**Sektör:** Bankacılık  
**Tarih:** 2026-11-25  

---

## 1. Senaryo

**Senaryo Adı:** Piyasa Olayları ve Döviz Dalgalanmalarına Göre Şüpheli Bankacılık İşlemleri Tespiti (AML & Anomali Analizi)

**Açıklama:**  
Bankacılık simülasyonumuzda müşterilerin para transferi, döviz alım-satım ve ani mevduat hareketleri gibi finansal işlemleri; dış piyasadaki anlık gelişmelerle (TCMB döviz kuru sıçramaları, KAP şirket ve bankacılık bildirimleri) karşılaştırılır.  
* Piyasada döviz kuru fırladığında veya KAP'ta büyük bir şirket gelişmesi duyurulduğunda yapılan işlemler **"normal piyasa tepkisi"** olarak kabul edilir.
* Ancak piyasada hiçbir kur hareketi veya haber **yokken** olağanüstü yüksek hacimli döviz alımı/transferi yapılması ya da hesap hareketlerinin aniden müşteri ortalamasının katbekat üstüne çıkması durumunda işlemler yapay zekâ ajanları tarafından denetlenip **"Açıklanamayan / Şüpheli İşlem"** olarak işaretlenir ve gerekçeli bir denetim raporuna dönüştürülür.

---

## 2. Ajan Tanımları

* **Ajan 1 (Dış Veri Toplayıcı):** TCMB günlük döviz kurlarını ve KAP kamuya açık piyasa bildirimlerini web kazıma ve tarayıcı otomasyonu (Playwright) ile çekip temizleyerek zaman damgalı standart formatta Ajan 2'ye teslim eder.
* **Ajan 2 (İş Mantığı ve Korelasyon):** Ajan 1'den gelen piyasa olayları ile bankanın sentetik hesap ve işlem kayıtlarını zaman ve tutar bazında eşleştirir; piyasa hareketleriyle uyuşmayan ani finansal hareketleri analiz eder.
* **Ajan 3 (Denetim, Kalite ve Raporlama):** Ajan 2'den gelen analiz sonuçlarını girdi kalitesi açısından denetler, açıklanamayan şüpheli işlemleri gerekçelendirip kaynak bağlantısıyla etiketler ve nihai denetim raporunu üretir (veri tutarsız veya bayatsa işi gerekçesiyle geri gönderir).

---

## 3. Web Kaynakları Listesi

| Kaynak Adı | Web Adresi (URL) | Alınacak Veri | Tarayıcı Gerekli mi? | robots.txt ve Kullanım Şartları Kontrolü |
| :--- | :--- | :--- | :--- | :--- |
| **TCMB Günlük Kurlar** | `https://www.tcmb.gov.tr/kurlar/today.xml` | Gösterge niteliğindeki döviz kurları (USD/TRY, EUR/TRY alış/satış ve efektif kurlar) | Hayır (Doğrudan XML/HTTP isteği) | Kamuya açık finansal veri bültenidir. robots.txt kontrol edildi, veri çekilmesinde engel bulunmamaktadır. |
| **KAP (Kamuyu Aydınlatma Platformu)** | `https://www.kap.org.tr` | Kamuyu aydınlatma bildirimleri, şirket ve banka haberleri, sermaye artırımı/temettü olayları | **Evet (Zorunlu)** (Sayfa dinamik JavaScript ile render edilmektedir; Playwright/headless Chrome kullanılacaktır) | Kamuya açık duyurulardır. robots.txt kurallarına uygun olarak istekler arasına bekleme (rate-limit / sleep) konularak taranacaktır. |

> **Kural Uyumu:** Kişisel veri (isim, profil vb.) toplanmayacaktır. Yalnızca herkese açık piyasa kurları ve şirket bildirimleri çekilecektir.

---

## 4. Rol Dağılımı

| Rol | Ad Soyad | GitHub Kullanıcı Adı | Sorumluluk Alanı |
| :--- | :--- | :--- | :--- |
| **Çekirdek ve Arayüz** | Melih Yavuk | `@melihyavuk` | ACP bağlantısı, ajanları çalıştırma, ilerleme ve izin onay ekranı, oturum kayıtları (log) |
| **Ajan 1** | Hiranur Doğan | `@dgnHira` | Web verisi toplama (TCMB & KAP), Playwright tarayıcı kullanımı, veri temizleme ve teslim |
| **Ajan 2** | Rüveyda Başboğa | `@basbogaruveyda-afk` | İş mantığı, sentetik banka verisi ile piyasa verilerini eşleştirme ve anomali analizi |
| **Ajan 3** | Gürol Pekmezci | `@GurolPekmezci` | Kalite denetimi, doğrulama, açıklanamayan işlemleri işaretleme ve gerekçeli nihai rapor |

---

## 5. Abonelik Bildirimi

| Üye | Rol | Bildirilen Yapay Zekâ Araçları / Abonelikler |
| :--- | :--- | :--- |
| **Hiranur Doğan** | Ajan 1 | Claude, Gemini |
| **Rüveyda Başboğa** | Ajan 2 | ChatGPT, Gemini |
| **Gürol Pekmezci** | Ajan 3 | Gemini |
| **Melih Yavuk** | Çekirdek ve Arayüz | Gemini |
