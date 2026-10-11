# Açık Kaynak Proje Keşif Raporu
## Tennis Analysis System – Tenis Maçı Analiz Sistemi

### 1. Depo Adı ve Bağlantısı

**Proje Adı:** Tennis Analysis System

**GitHub Deposu:** https://github.com/ameynarwadkar/Tennis-Analysis-System

**Proje Alanı:** Yapay Zekâ, Bilgisayarlı Görü, Derin Öğrenme ve Spor Analitiği

**Kullanılan Teknolojiler:** Python, YOLOv8, ResNet50 ve görüntü işleme teknikleri.

### 2. Projenin Çözdüğü Problem

Tenis maçlarında oyuncuların saha içerisindeki hareketlerini, topun izlediği yolu ve hız değişimlerini analiz etmek, özellikle manuel yöntemlerle yapıldığında oldukça zaman alıcıdır. Bu tür analizlerin yapılabilmesi için maç görüntülerinin ayrıntılı şekilde incelenmesi ve oyuncuların performanslarının değerlendirilmesi gerekir.

Tennis Analysis System, bu süreci bilgisayarlı görü ve derin öğrenme teknolojileriyle otomatikleştirmeyi amaçlayan açık kaynaklı bir projedir. Sistem, tenis maçlarının video görüntülerini işleyerek oyuncuları ve tenis topunu tespit eder, hareketlerini takip eder ve hız bilgilerini hesaplar. Ayrıca kort üzerindeki konumları görselleştirerek maçın daha kolay analiz edilmesini sağlar.

Bu sayede yalnızca maç görüntülerini izlemek yerine, görüntülerden elde edilen sayısal ve görsel veriler üzerinden oyuncu performansını değerlendirmek mümkün hale gelir.

### 3. Projenin Güçlü Yanları

**1. Yapay Zekâ ile Oyuncu ve Top Tespiti**

Projenin en önemli özelliklerinden biri, YOLOv8 nesne tespit modelini kullanarak tenis oyuncularını video görüntüleri üzerinde belirleyebilmesidir. Tenis topu küçük ve hızlı hareket eden bir nesne olduğu için tespit edilmesi daha zordur. Bu nedenle projede YOLO modelinin tenis topu tespiti için ayrıca eğitilmesi yaklaşımı kullanılmıştır.

Bu özellik, oyuncuların ve topun hareketlerinin otomatik olarak takip edilmesine yardımcı olur.

**2. Hız Hesaplama ve Performans Analizi**

Sistem, oyuncuların hareket hızlarını ve tenis topunun hızını hesaplamaya yönelik algoritmalar içerir. Bu sayede video görüntülerinden yalnızca nesnelerin konumları değil, performans değerlendirmesinde kullanılabilecek sayısal bilgiler de elde edilir.

Örneğin oyuncuların kort üzerindeki hareketleri ve topun hızı, maçın temposunu değerlendirmek için kullanılabilir. Bu özellik, görüntü işleme sonuçlarının veri analiziyle birleştirilmesi açısından önemlidir.

**3. Mini Kort Oluşturma ve Görselleştirme**

Projede dikkatimi çeken özelliklerden biri de mini tenis kortu oluşturulmasıdır. Sistem, oyuncuların gerçek kort üzerindeki konumlarını daha küçük bir kort gösterimine aktararak hareketlerinin görsel olarak takip edilmesini amaçlar.

Ayrıca ResNet50 modelinin son katmanı özel bir veri seti üzerinde eğitilerek kortun önemli noktalarının belirlenmesi sağlanır. Böylece oyuncuların saha içerisindeki konumlarının anlaşılması ve hareketlerinin analiz edilmesi kolaylaşır.

### 4. Kendi Projemde Kullanabileceğim Fikir

Bu projede en çok ilgimi çeken yaklaşım, video görüntülerinden elde edilen bilgilerin anlamlı verilere dönüştürülmesi ve kullanıcıya görsel olarak sunulması oldu.

Kendi geliştireceğim bir projede de benzer şekilde kamera görüntülerinden nesne veya insan hareketlerini tespit eden bir sistem oluşturabilirim. Örneğin sporcuların hareketlerini takip eden, belirli hareketlerin tekrar sayılarını hesaplayan ve elde edilen sonuçları grafiklerle gösteren bir uygulama geliştirilebilir.

Bu projeden özellikle yapay zekâ modellerinin görüntü işleme süreçlerinde kullanılması, elde edilen verilerin analiz edilmesi ve sonuçların kullanıcıya anlaşılır şekilde sunulması konularında yararlanabileceğimi düşünüyorum.

