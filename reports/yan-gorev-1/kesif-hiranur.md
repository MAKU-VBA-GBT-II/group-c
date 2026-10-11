# Açık Kaynak Proje Keşif Raporu

## Tennis Analysis System – Tenis Maçı Analiz Sistemi

### 1. Depo Adı ve Bağlantısı

**Depo Adı:** Tennis Analysis System

**GitHub Bağlantısı:** https://github.com/ameynarwadkar/Tennis-Analysis-System

**Kullanılan Teknolojiler:** Python, YOLOv8, ResNet50, Bilgisayarlı Görü ve Derin Öğrenme

### 2. Çözdüğü Problem

Tenis maçlarında oyuncuların hareketlerini, topun konumunu ve hızını manuel olarak takip edip analiz etmek zaman alıcı ve zahmetli bir süreçtir. Tennis Analysis System, bilgisayarlı görü ve derin öğrenme yöntemlerini kullanarak maç videolarındaki oyuncuları ve topu otomatik olarak tespit etmeyi, hareketlerini takip etmeyi ve hızlarını hesaplamayı amaçlamaktadır. Ayrıca oyuncuların kort üzerindeki konumlarını görselleştirerek maçların daha ayrıntılı incelenmesine ve performans analizinin kolaylaştırılmasına yardımcı olur.

### 3. Projenin Güçlü Yanları

- **Yapay zekâ destekli oyuncu ve top tespiti:** YOLOv8 modelini kullanarak oyuncuları tespit ederken, tenis topunun daha doğru algılanabilmesi için özel olarak eğitilmiş bir YOLO modelinden yararlanması, projenin güçlü yönlerinden biridir.

- **Hız hesaplama ve performans analizi:** Oyuncuların hareket hızlarını ve tenis topunun hızını hesaplayarak maç görüntülerinden sayısal veriler elde edilmesini sağlar. Bu veriler, oyuncuların performansını ve maçın temposunu değerlendirmek için kullanılabilir.

- **Mini kort oluşturma ve görselleştirme:** ResNet50 modeliyle kortun önemli noktalarını belirleyerek oyuncuların konumlarını mini bir tenis kortu üzerinde gösterir. Bu özellik, hareketlerin ve saha içindeki konumların daha anlaşılır şekilde incelenmesini sağlar.

### 4. Kendi Projemde Kullanabileceğim Fikir

- Bu projede kullanılan görüntü işleme, nesne tespiti ve hareket takibi yöntemlerinden yararlanarak kamera görüntüleri üzerinden sporcuların hareketlerini analiz eden bir uygulama geliştirilebilir. Örneğin, sporcuların hareketlerini otomatik olarak algılayan, tekrar sayılarını hesaplayan ve elde edilen sonuçları grafiklerle kullanıcıya sunan bir sistem oluşturulabilir.