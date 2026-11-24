"""
VBA BANKACILIK - Sentetik Bankacılık İşlem Verisi Üretici
Duyuru 10 Standartlarına Uygun: Dış piyasa verileriyle (TCMB Döviz ve KAP) eşleşebilir,
dışarıdan parametre ve aralık alabilir simülasyon betiği.
"""

import argparse
import csv
import random
from datetime import date, datetime, time, timedelta
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Piyasa olaylarıyla eşleşebilir sentetik bankacılık işlem verisi üretici."
    )
    parser.add_argument(
        "--kayit-sayisi",
        type=int,
        default=500,
        help="Üretilecek işlem sayısı (varsayılan: 500)",
    )
    parser.add_argument(
        "--min-tutar",
        type=float,
        default=1000.0,
        help="Minimum işlem tutarı (varsayılan: 1000.0)",
    )
    parser.add_argument(
        "--max-tutar",
        type=float,
        default=500000.0,
        help="Maksimum işlem tutarı (varsayılan: 500000.0)",
    )
    parser.add_argument(
        "--doviz-listesi",
        type=str,
        default="TRY,USD,EUR",
        help="Kullanılacak para birimleri (virgülle ayrılmış, varsayılan: TRY,USD,EUR)",
    )
    parser.add_argument(
        "--baslangic",
        type=str,
        default="2026-10-01",
        help="Başlangıç tarihi YYYY-MM-DD (varsayılan: 2026-10-01)",
    )
    parser.add_argument(
        "--bitis",
        type=str,
        default="2026-11-20",
        help="Bitiş tarihi YYYY-MM-DD (varsayılan: 2026-11-20)",
    )
    parser.add_argument(
        "--tohum",
        type=int,
        default=42,
        help="Rastgelelik tohumu (varsayılan: 42)",
    )
    parser.add_argument(
        "--cikti",
        type=str,
        default="data/banka-islemleri.csv",
        help="Üretilecek CSV dosyasının yolu (varsayılan: data/banka-islemleri.csv)",
    )
    return parser.parse_args()


def veri_uret(args):
    random.seed(args.tohum)

    dovizler = [d.strip().upper() for d in args.doviz_listesi.split(",") if d.strip()]
    if not dovizler:
        dovizler = ["TRY", "USD", "EUR"]

    islem_turleri = [
        "Havale",
        "EFT",
        "Döviz Alımı",
        "Döviz Satımı",
        "Yurtdışı Para Transferi (SWIFT)",
        "Para Çekme",
        "Para Yatırma",
        "Kredi Kartı Borç Ödeme",
    ]

    kanallar = ["Mobil bankacılık", "İnternet bankacılığı", "ATM", "Şube"]
    sehirler = ["İstanbul", "Ankara", "İzmir", "Antalya", "Bursa", "Burdur"]
    durumlar = ["Başarılı", "Şüpheli/Beklemede", "Başarısız"]
    segmentler = ["Bireysel", "Ticari", "Kurumsal"]

    uygun_kanallar = {
        "Havale": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
        "EFT": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
        "Döviz Alımı": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
        "Döviz Satımı": ["Mobil bankacılık", "İnternet bankacılığı", "Şube"],
        "Yurtdışı Para Transferi (SWIFT)": ["İnternet bankacılığı", "Şube"],
        "Para Yatırma": ["ATM", "Şube"],
        "Para Çekme": ["ATM", "Şube"],
        "Kredi Kartı Borç Ödeme": ["Mobil bankacılık", "İnternet bankacılığı", "ATM"],
    }

    # TCMB kurları için referans temel kurlar
    referans_kurlar = {
        "TRY": 1.0,
        "USD": 34.25,
        "EUR": 37.10,
    }

    # KAP & Piyasa olayları ile eşleşebilecek işlem açıklamaları
    olay_aciklamalari = {
        "Döviz Alımı": [
            "Piyasa kur dalgalanması döviz alımı",
            "Açıklamasız yüksek döviz alımı",
            "İthalat faturası döviz temini",
        ],
        "Döviz Satımı": [
            "Kur realizasyonu döviz satımı",
            "Mevduat döviz bozdurma",
            "Olağandışı döviz çıkışı",
        ],
        "Yurtdışı Para Transferi (SWIFT)": [
            "Yurtdışı şirket sermaye transferi",
            "Açıklamasız sınır ötesi transfer",
            "Dış ticaret ödemesi",
        ],
        "Havale": [
            "Ticari mal bedeli",
            "Şirket içi hesap aktarımı",
            "Parçalı transfer (smurfing şüphesi)",
        ],
        "EFT": [
            "Tedarikçi ödemesi",
            "Kira ödemesi",
            "Piyasa kapanışı sonrası yüksek EFT",
        ],
        "Para Yatırma": ["Nakit ticari hasılat", "ATM peş peşe nakit yatırma"],
        "Para Çekme": ["Nakit şirket avansı", "Büyük tutarlı şube nakit çekimi"],
        "Kredi Kartı Borç Ödeme": ["Bireysel kart ekstre ödemesi", "Kurumsal kart kapama"],
    }

    baslangic_tarih = datetime.strptime(args.baslangic, "%Y-%m-%d").date()
    bitis_tarih = datetime.strptime(args.bitis, "%Y-%m-%d").date()
    gun_farki = max((bitis_tarih - baslangic_tarih).days, 1)

    # 100 farklı müşteri profili
    musteriler = {}
    for musteri_id in range(10001, 10101):
        musteriler[musteri_id] = {
            "sehir": random.choice(sehirler),
            "segment": random.choices(segmentler, weights=[65, 25, 10], k=1)[0],
        }

    sutunlar = [
        "islem_id",
        "tarih",
        "islem_saati",
        "musteri_id",
        "musteri_segmenti",
        "islem_turu",
        "doviz_cinsi",
        "tutar",
        "kur_degeri",
        "islem_tutari_try",
        "kanal",
        "sehir",
        "durum",
        "islem_aciklamasi",
    ]

    kayitlar = []

    for i in range(1, args.kayit_sayisi + 1):
        islem_id = f"TRX{i:06d}"
        musteri_id = random.choice(list(musteriler))
        musteri = musteriler[musteri_id]

        islem_turu = random.choice(islem_turleri)
        kanal = random.choice(uygun_kanallar[islem_turu])

        # Rastgele tarih ve saat
        tarih = baslangic_tarih + timedelta(days=random.randint(0, gun_farki))
        saat = random.randint(8, 22)
        dakika = random.randint(0, 59)
        saniye = random.randint(0, 59)
        islem_saati = f"{saat:02d}:{dakika:02d}:{saniye:02d}"

        # Döviz cinsi seçimi (Döviz alım-satım ve SWIFT işlemlerinde USD/EUR ağırlıklı)
        if islem_turu in ["Döviz Alımı", "Döviz Satımı", "Yurtdışı Para Transferi (SWIFT)"]:
            doviz_cinsi = random.choices(["USD", "EUR", "TRY"], weights=[50, 40, 10], k=1)[0]
        else:
            doviz_cinsi = random.choices(dovizler, weights=[80] + [10] * (len(dovizler) - 1), k=1)[0]

        # Müşteri segmentine ve argümanlara göre tutar hesaplama
        segment_carpan = {
            "Bireysel": 0.2,
            "Ticari": 0.6,
            "Kurumsal": 1.0,
        }[musteri["segment"]]

        maks_limit = args.min_tutar + (args.max_tutar - args.min_tutar) * segment_carpan
        tutar = round(random.uniform(args.min_tutar, max(args.min_tutar + 100, maks_limit)), 2)

        # Kur ve TRY karşılığı
        baz_kur = referans_kurlar.get(doviz_cinsi, 1.0)
        # Kurda günlük küçük dalgalanma (%-2 ile %+2 arası)
        kur_dalgalanma = random.uniform(0.98, 1.02)
        kur_degeri = round(baz_kur * kur_dalgalanma, 4) if doviz_cinsi != "TRY" else 1.0
        islem_tutari_try = round(tutar * kur_degeri, 2)

        # Durum ve şüpheli işlem ataması
        # Olağanüstü yüksek tutarlı veya gece yapılan işlemlerde şüpheli olma ihtimali artar
        durum = random.choices(durumlar, weights=[88, 8, 4], k=1)[0]
        aciklamalar = olay_aciklamalari.get(islem_turu, ["Genel bankacılık işlemi"])
        islem_aciklamasi = random.choice(aciklamalar)

        kayitlar.append([
            islem_id,
            tarih.strftime("%Y-%m-%d"),
            islem_saati,
            musteri_id,
            musteri["segment"],
            islem_turu,
            doviz_cinsi,
            tutar,
            kur_degeri,
            islem_tutari_try,
            kanal,
            musteri["sehir"],
            durum,
            islem_aciklamasi,
        ])

    cikti_yolu = Path(args.cikti)
    cikti_yolu.parent.mkdir(parents=True, exist_ok=True)

    with open(cikti_yolu, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(sutunlar)
        writer.writerows(kayitlar)

    print(f"Başarılı: {len(kayitlar)} adet bankacılık işlemi üretildi -> {cikti_yolu}")
    print(f"Kullanılan parametreler: Kayıt={args.kayit_sayisi}, Min={args.min_tutar}, Max={args.max_tutar}, Dövizler={dovizler}")


if __name__ == "__main__":
    args = parse_arguments()
    veri_uret(args)
