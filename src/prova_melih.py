import os
import random

sayilar = [random.randint(1, 100) for _ in range(10)]
os.makedirs('data', exist_ok=True)

with open('data/prova-melih.csv', 'w', encoding='utf-8') as f:
  f.write('deger\n')
  for sayi in sayilar:
    f.write(f'{sayi}\n')

print('Dosya oluşturuldu!')