
import random
import csv
from pathlib import Path

# Proje ana klasörünü bul
proje_dizini = Path(__file__).resolve().parent.parent

# 1 ile 100 arasında 10 rastgele sayı üret
sayilar = [random.randint(1, 100) for _ in range(10)]

# CSV dosyasının yolu
dosya_yolu = proje_dizini / "data" / "prova-melih.csv"

# Sayıları CSV dosyasına yaz
with open(dosya_yolu, "w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)

    # Sütun başlığı
    yazici.writerow(["deger"])

    # 10 sayıyı alt alta yaz
    for sayi in sayilar:
        yazici.writerow([sayi])

print("Dosya başarıyla oluşturuldu!")
print("Dosya yolu:", dosya_yolu)
print("Üretilen sayılar:", sayilar)