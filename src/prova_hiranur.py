import random

# 1-100 arasında 10 rastgele sayı üretip data/prova-hiranur.csv dosyasına yazalım
sayilar = [random.randint(1, 100) for _ in range(10)]

with open("data/prova-hiranur.csv", "w", encoding="utf-8") as f:
    f.write("deger\n")
    for sayi in sayilar:
        f.write(f"{sayi}\n")

print("İşlem tamamlandı.")