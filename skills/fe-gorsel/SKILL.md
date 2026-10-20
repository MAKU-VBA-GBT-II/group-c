# FE Görselleştirme Becerisi

## Amaç
Banka işlem verilerini anlaşılır ve doğru grafiklerle görselleştirmek.

## Adımlar
1. data/banka-islemleri.csv dosyasını pandas ile oku.
2. Tarih ve tutar sütunlarını kontrol et.
3. Günlük toplam işlem tutarını çizgi grafikle göster.
4. Müşteri segmentlerine göre işlem sayılarını sütun grafikle göster.
5. Grafiklere başlık, eksen adları ve ölçü birimleri ekle.
6. Grafikleri PNG biçiminde visuals klasörüne kaydet.
7. Oluşturulan dosyaları kontrol et.

## Kullanılan dosyalar
- Girdi: data/banka-islemleri.csv
- Çıktı: visuals/gunluk-islem-tutari.png
- Çıktı: visuals/musteri-segmenti.png

## Çalıştırma
Proje ana klasöründe şu komutla grafikler oluşturulur:
python src/generate_visuals.py

## Gerekli kütüphaneler
pandas ve matplotlib
