
import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

# Dosya yolları
veri_dosyasi = Path("data/banka-islemleri.csv")
rapor_dosyasi = Path("docs/analiz-g1.md")

# Veriyi oku
with veri_dosyasi.open("r", encoding="utf-8-sig", newline="") as dosya:
    okuyucu = csv.DictReader(dosya)
    veriler = list(okuyucu)

if not veriler:
    raise ValueError("CSV dosyasında analiz edilecek kayıt bulunamadı.")

# Temel alanları dönüştür
for kayit in veriler:
    kayit["tutar"] = float(kayit["tutar"])
    kayit["islem_suresi_sn"] = int(kayit["islem_suresi_sn"])

toplam_islem = len(veriler)
ortalama_tutar = mean(k["tutar"] for k in veriler)
ortalama_sure = mean(k["islem_suresi_sn"] for k in veriler)

# Kategorik kırılımlar
islem_turu_sayisi = Counter(k["islem_turu"] for k in veriler)
segment_sayisi = Counter(k["musteri_segmenti"] for k in veriler)

# Başarılı işlemlerin tutarlarını kullanarak hacim hesapla
basarili = [k for k in veriler if k["durum"] == "Başarılı"]
basarili_hacim = defaultdict(float)

for kayit in basarili:
    basarili_hacim[kayit["islem_turu"]] += kayit["tutar"]

ilk_uc = sorted(
    basarili_hacim.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

# Diğer kalite kontrolleri
benzersiz_id = len({k["islem_id"] for k in veriler})
durum_sayisi = Counter(k["durum"] for k in veriler)
basarili_toplam = sum(k["tutar"] for k in basarili)

# Raporu hazırla
rapor = [
    "# G1 Veri Analizi Raporu",
    "",
    "## 1. Veri setinin özeti",
    "",
    f"- Toplam kayıt: **{toplam_islem}**",
    f"- Sütun sayısı: **{len(veriler[0])}**",
    f"- Benzersiz işlem ID sayısı: **{benzersiz_id}**",
    f"- Başarılı işlem sayısı: **{len(basarili)}**",
    f"- Başarılı işlemlerin toplam tutarı: **{basarili_toplam:,.2f} TL**",
    "",
    "## 2. Metrikler ve yorumlar",
    "",
    "### Metrik 1 — Toplam işlem sayısı",
    "",
    f"- Sonuç: **{toplam_islem} işlem**",
    "- Yorum: Bu sayı, veri setindeki başarılı, başarısız ve beklemedeki tüm işlem kayıtlarını kapsar.",
    "",
    "### Metrik 2 — Ortalama işlem tutarı",
    "",
    f"- Sonuç: **{ortalama_tutar:,.2f} TL**",
    "- Yorum: Ortalama, tüm kayıtların tutarları üzerinden hesaplanmıştır. Başarısız veya beklemedeki işlemler de bu metrikte yer alır.",
    "",
    "### Metrik 3 — İşlem türlerine göre dağılım",
    "",
]

for tur, sayi in islem_turu_sayisi.most_common():
    rapor.append(f"- {tur}: **{sayi} işlem** (%{sayi / toplam_islem * 100:.1f})")

rapor.extend([
    "",
    "- Yorum: Bu dağılım, hangi işlem türlerinin daha sık kullanıldığını gösterir; tek başına finansal hacmi göstermez.",
    "",
    "### Metrik 4 — Müşteri segmentlerine göre dağılım",
    "",
])

for segment, sayi in segment_sayisi.most_common():
    rapor.append(f"- {segment}: **{sayi} işlem** (%{sayi / toplam_islem * 100:.1f})")

rapor.extend([
    "",
    "- Yorum: Segment dağılımı, işlem kayıtlarının müşteri gruplarına göre nasıl dağıldığını gösterir. İşlem sayısı, benzersiz müşteri sayısı ile aynı değildir.",
    "",
    "### Metrik 5 — Başarılı işlem hacminde ilk üç işlem türü",
    "",
])

for sira, (tur, tutar) in enumerate(ilk_uc, start=1):
    rapor.append(f"{sira}. **{tur}** — {tutar:,.2f} TL")

rapor.extend([
    "",
    "- Yorum: Sıralama yalnızca başarılı işlemlerin tutar toplamına göre yapılmıştır. Başarısız ve beklemedeki işlemler finansal hacme dahil edilmemiştir.",
    "",
    "### Ek metrik — Ortalama işlem süresi",
    "",
    f"- Sonuç: **{ortalama_sure:.2f} saniye**",
    "- Yorum: Bu değer tüm işlemlerin ortalama süresidir. Kanal ve işlem türüne göre ayrıca incelenmesi performans sorunlarını ortaya çıkarabilir.",
    "",
    "## 3. Somut gözlemler",
    "",
    f"1. Veri setinde toplam **{toplam_islem} işlem** bulunmaktadır.",
    f"2. En sık görülen işlem türü **{islem_turu_sayisi.most_common(1)[0][0]}** olup {islem_turu_sayisi.most_common(1)[0][1]} kayıt içerir.",
    f"3. En fazla işlem kaydı bulunan müşteri segmenti **{segment_sayisi.most_common(1)[0][0]}** segmentidir ({segment_sayisi.most_common(1)[0][1]} kayıt).",
    "",
    "## 4. Önerilen eylem",
    "",
    "Başarısız ve beklemedeki işlemler kanal ve işlem türüne göre ayrıca incelenmelidir. Başarısızlık oranı belirli bir kanalda yükseliyorsa ilgili süreç araştırılmalı; işlem hacmi değerlendirmelerinde yalnızca başarılı işlemlerin tutarları kullanılmalıdır.",
    "",
    "## 5. Veri kontrol notları",
    "",
    f"- Benzersiz işlem ID sayısı: {benzersiz_id} / {toplam_islem}",
    f"- Durum dağılımı: {dict(durum_sayisi)}",
    "- Bu rapor sentetik eğitim verisine dayanır; gerçek banka istatistiklerini temsil etmez.",
    "",
])

rapor_dosyasi.parent.mkdir(parents=True, exist_ok=True)
rapor_dosyasi.write_text("\n".join(rapor), encoding="utf-8")

print("Analiz tamamlandı.")
print(f"Toplam işlem: {toplam_islem}")
print(f"Ortalama tutar: {ortalama_tutar:.2f} TL")
print(f"Başarılı işlem hacmi: {basarili_toplam:.2f} TL")
print(f"Rapor oluşturuldu: {rapor_dosyasi}")
