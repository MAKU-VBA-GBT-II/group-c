
import csv
import random
from datetime import date, timedelta
from pathlib import Path

# 1. Sabit tohum: Her çalıştırmada aynı veriyi üretir.
random.seed(42)

# 2. Veri setimizin temel özellikleri
KAYIT_SAYISI = 500

ISLEM_TURLERI = [
    "Havale",
    "EFT",
    "Para yatırma",
    "Para çekme",
    "Fatura ödeme",
    "Kredi taksiti ödeme",
    "Kredi kartı borç ödeme"
]

KANALLAR = [
    "Mobil bankacılık",
    "İnternet bankacılığı",
    "ATM",
    "Şube"
]

SEHIRLER = [
    "İstanbul", "Ankara", "İzmir",
    "Antalya", "Bursa", "Burdur"
]

DURUMLAR = ["Başarılı", "Başarısız", "Beklemede"]
SEGMENTLER = ["Bireysel", "Ticari", "Kurumsal"]

SUTUNLAR = [
    "islem_id", "tarih", "musteri_id",
    "islem_turu", "tutar", "kanal",
    "sehir", "durum", "musteri_segmenti",
    "islem_suresi_sn"
]

# 3. İşlem türüne uygun kanallar
UYGUN_KANALLAR = {
    "Havale": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
    "EFT": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
    "Para yatırma": ["ATM", "Şube"],
    "Para çekme": ["ATM", "Şube"],
    "Fatura ödeme": KANALLAR,
    "Kredi taksiti ödeme": KANALLAR,
    "Kredi kartı borç ödeme": KANALLAR
}

# 4. Tarih aralığı
BASLANGIC = date(2026, 1, 1)
BITIS = date(2026, 9, 30)
GUN_SAYISI = (BITIS - BASLANGIC).days

# 5. Aynı müşterinin bilgileri tutarlı kalsın.
musteriler = {}

for musteri_id in range(10001, 10101):
    musteriler[musteri_id] = {
        "sehir": random.choice(SEHIRLER),
        "segment": random.choices(
            SEGMENTLER, weights=[70, 25, 5], k=1
        )[0]
    }

# 6. Banka işlemlerini üret
kayitlar = []

for i in range(KAYIT_SAYISI):
    musteri_id = random.choice(list(musteriler))
    musteri = musteriler[musteri_id]

    islem_turu = ISLEM_TURLERI[i % len(ISLEM_TURLERI)]
    kanal = random.choice(UYGUN_KANALLAR[islem_turu])

    tarih = BASLANGIC + timedelta(
        days=random.randint(0, GUN_SAYISI)
    )

    # Müşteri segmentine göre işlem tutarı
    tutar_ust_sinir = {
        "Bireysel": 20000,
        "Ticari": 60000,
        "Kurumsal": 100000
    }[musteri["segment"]]

    tutar = round(random.uniform(10, tutar_ust_sinir), 2)

    durum = random.choices(
        DURUMLAR, weights=[90, 7, 3], k=1
    )[0]

    # Dijital işlemler genellikle daha kısa sürer.
    if kanal in ["Mobil bankacılık", "İnternet bankacılığı"]:
        sure = random.randint(5, 180)
    elif kanal == "ATM":
        sure = random.randint(30, 300)
    else:
        sure = random.randint(180, 1800)

    kayitlar.append({
        "islem_id": 1001 + i,
        "tarih": tarih.isoformat(),
        "musteri_id": musteri_id,
        "islem_turu": islem_turu,
        "tutar": f"{tutar:.2f}",
        "kanal": kanal,
        "sehir": musteri["sehir"],
        "durum": durum,
        "musteri_segmenti": musteri["segment"],
        "islem_suresi_sn": sure
    })

# 7. Tarihe göre sırala
kayitlar.sort(key=lambda kayit: kayit["tarih"])

# 8. Verileri doğrula
assert len(kayitlar) == 500
assert all(len(kayit) == 10 for kayit in kayitlar)
assert len({k["islem_id"] for k in kayitlar}) == 500
assert set(k["islem_turu"] for k in kayitlar) == set(ISLEM_TURLERI)
assert all(10 <= float(k["tutar"]) <= 100000 for k in kayitlar)
assert all(5 <= k["islem_suresi_sn"] <= 1800 for k in kayitlar)
assert all(BASLANGIC <= date.fromisoformat(k["tarih"]) <= BITIS for k in kayitlar)

# 9. CSV dosyasını oluştur
proje_klasoru = Path(__file__).resolve().parent.parent
dosya_yolu = proje_klasoru / "data" / "banka-islemleri.csv"
dosya_yolu.parent.mkdir(parents=True, exist_ok=True)

with open(dosya_yolu, "w", newline="", encoding="utf-8-sig") as dosya:
    yazici = csv.DictWriter(dosya, fieldnames=SUTUNLAR)
    yazici.writeheader()
    yazici.writerows(kayitlar)

print("Sentetik banka verileri başarıyla üretildi!")
print(f"Kayıt sayısı: {len(kayitlar)}")
print(f"Sütun sayısı: {len(SUTUNLAR)}")
print(f"İşlem türü sayısı: {len(ISLEM_TURLERI)}")
print("Rastgelelik tohumu: 42")
print(f"CSV dosyası: {dosya_yolu}")
print("İlk veri doğrulama kontrolleri başarılı.")
 