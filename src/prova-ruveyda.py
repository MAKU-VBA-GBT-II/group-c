import random
import os
sayilar = [random.randint(1, 100) for _ in range(10)]
os.makedirs('data', exist_ok=True)
with open('data/prova-ruveyda.csv', 'w', encoding='utf-8') as f:
    f.write('deger\n')
    for s in sayilar: f.write(f'{s}\n')
print('Hazýr!')
