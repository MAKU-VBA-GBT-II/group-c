# Issue #12 — Kanıt yorumu taslağı

BE veri üretimi teslim kanıtı: commit [8e2c25c](https://github.com/MAKU-VBA-GBT-II/group-c/commit/8e2c25c).

Kanıt: `skills/be-veri/SKILL.md` becerisini kullanarak Codex ile ürettim.

- Veri dosyası: [`data/banka-islemleri.csv`](https://github.com/MAKU-VBA-GBT-II/group-c/blob/8e2c25c/data/banka-islemleri.csv). Başlık hariç **500 veri satırı**, **10 sütun** ve **7 işlem türü** içerir. Başlıkla birlikte toplam 501 CSV satırıdır.
- Üretim kodu: [`src/banka_veri_uret.py`](https://github.com/MAKU-VBA-GBT-II/group-c/blob/8e2c25c/src/banka_veri_uret.py). Sabit rastgelelik tohumu `42`, çıktı kodlaması `utf-8-sig` (BOM'lu UTF-8) olarak kullanılmıştır.
- Veri sözlüğü: [`docs/veri-sozlugu-g1.md`](https://github.com/MAKU-VBA-GBT-II/group-c/blob/8e2c25c/docs/veri-sozlugu-g1.md).
- BE skill dosyası: [`skills/be-veri/SKILL.md`](https://github.com/MAKU-VBA-GBT-II/group-c/blob/8e2c25c/skills/be-veri/SKILL.md).

**Dosya adı farkı:** Kabul kriterinde `bankacilik-verisi.csv` adı belirtilirken teslim edilen dosya `data/banka-islemleri.csv` adıyla kaydedilmiştir. Üretim kodu, veri sözlüğü ve skill dosyasındaki yollar bu mevcut adı kullanmaktadır. Bu, kabul kriterindeki dosya adıyla teslim arasında bir adlandırma farkıdır; dosyanın adı değiştirilmemiştir. İncelemede yukarıdaki mevcut dosya bağlantısı kullanılabilir.

**Skill düzeltmesi:** Skill dosyasındaki `UTF-8` ifadesi `UTF-8 (BOM'lu, utf-8-sig)` olarak düzeltildi. Bu düzeltme yukarıdaki veri teslim commit'i `8e2c25c` sonrasında ayrı bir commit ile yapılmıştır. Güncel dosya: [`skills/be-veri/SKILL.md`](https://github.com/MAKU-VBA-GBT-II/group-c/blob/main/skills/be-veri/SKILL.md).
