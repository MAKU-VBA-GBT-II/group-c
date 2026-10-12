
import csv
import random
from pathlib import Path

# data klasörü yoksa oluştur
Path("data").mkdir(exist_ok=True)

# 1 ile 100 arasında 10 rastgele sayı üret
sayilar = [random.randint(1, 100) for _ in range(10)]

# Sayıları CSV dosyasına yaz
with open("data/prova-gurol.csv", "w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["deger"])

    for sayi in sayilar:
        yazici.writerow([sayi])

print("CSV dosyası başarıyla oluşturuldu!")
