import os
import random
import pandas as pd

# 1 ile 100 arasında 10 rastgele sayı üret
sayilar = [random.randint(1, 100) for _ in range(10)]

# Veriyi DataFrame yapısına getir (başlık 'deger' olacak)
df = pd.DataFrame({"deger": sayilar})

# data klasörünün var olduğundan emin ol
os.makedirs("data", exist_ok=True)

# CSV dosyasına kaydet
df.to_csv("data/prova-hiranur.csv", index=False)

print("Dosya başarıyla oluşturuldu ve kaydedildi.")