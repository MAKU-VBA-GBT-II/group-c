# Dönem Raporu 1 — Hiranur Doğan'ın Katkısı

**Üye / rol:** Hiranur Doğan (`dgnHira`) — BE

**Hazırlanma tarihi:** 3 Kasım 2026

**Amaç:** PM Rüveyda Başboğa'nın `reports/donem-raporu-1.md` raporuna kaynak olacak kişisel teslim ve öneri kaydı.

## 1. Ne teslim ettim?

| Teslim | Kanıt |
| --- | --- |
| Sabit `seed=42` ile 500 kayıt, 10 sütun ve 7 işlem türü içeren sentetik bankacılık verisi; üretim betiği ve veri sözlüğü | [#12 teslim yorumu](https://github.com/MAKU-VBA-GBT-II/group-c/issues/12#issuecomment-6397492031), [veri teslim commit'i](https://github.com/MAKU-VBA-GBT-II/group-c/commit/8e2c25c) |
| BE becerisinde çıktı kodlaması ve çalıştırma / teslim talimatlarının açıklanması | [#18](https://github.com/MAKU-VBA-GBT-II/group-c/issues/18), [main dalındaki talimat güncellemesi](https://github.com/MAKU-VBA-GBT-II/group-c/commit/89abb0e) |
| CSV doğrulama iyileştirmesi: geçersiz tarih, zorunlu alan ve sayısal değer kontrolleri; açıklayıcı hata mesajları ve hata durumunda mevcut raporun korunması | [#25 teslim ve test kanıtı](https://github.com/MAKU-VBA-GBT-II/group-c/issues/25#issuecomment-6438916336), [main dalındaki düzeltme](https://github.com/MAKU-VBA-GBT-II/group-c/commit/eae8822) |
| Grup D'nin `be-veri` becerisinin çapraz incelemesi; veri sözlüğüne giden göreli bağlantı için somut düzeltme önerisi | [Grup D #25 — kapalı inceleme](https://github.com/MAKU-VBA-GBT-II/group-d/issues/25), [uygulanan düzeltme](https://github.com/MAKU-VBA-GBT-II/group-d/commit/ca8719563f3410ad3fff437db21e7eff2c55808e) |
| CoastSnap-Toolbox keşif raporu ve derste sunulan reponun adı / bağlantısı | [Rapor güncellemesi](https://github.com/MAKU-VBA-GBT-II/group-c/commit/004419c), [ders reposundaki yanıtım](https://github.com/MAKU-VBA-GBT-II/ders/issues/3#issuecomment-6496256025) |

**Teslim açıklaması:** #12 kabul kriterindeki `bankacilik-verisi.csv` adı ile teslimde kullanılan `data/banka-islemleri.csv` adı arasındaki fark teslim yorumunda açıklandı. Üretim betiği ve belgelerde mevcut dosya yolu kullanılıyor.

## 2. Neye takıldım, nasıl aştım?

- **Yerel teslimin GitHub'a yansımaması:** CoastSnap raporu yerelde güncellenmiş olmasına rağmen GitHub'da tenis raporu görünüyordu. Yalnızca ilgili rapor güncellemesi güncel `main` üzerine alınarak gönderildi; [004419c](https://github.com/MAKU-VBA-GBT-II/group-c/commit/004419c) ile uzak depodaki dosya güncellendi.
- **Teslim bilgilerinin açıklığı:** CSV dosya adı farkını ve BOM'lu UTF-8 (`utf-8-sig`) kodlamasını teslim yorumunda belirttim; beceri talimatları da mevcut üretim akışına uygun biçimde netleştirildi. Kanıt: [#12 yorumu](https://github.com/MAKU-VBA-GBT-II/group-c/issues/12#issuecomment-6397492031) ve [89abb0e](https://github.com/MAKU-VBA-GBT-II/group-c/commit/89abb0e).

## 3. Sonraki dönem için önerim

Her teslimden sonra GitHub'daki dosyayı ve commit bağlantısını kontrol edip aynı gün ilgili issue'ya kanıt yorumu eklemeyi öneriyorum. Veri alışverişinden önce dosya adı, kodlama, alan adları ve doğrulama kurallarının partner takımla yazılı olarak netleştirilmesi de teslim hatalarını azaltabilir.

## 4. Görev 3 hazırlığına BE katkı önerisi

Grup D ile veri değişimi için aşağıdaki maddeleri öneriyorum; bunlar henüz partner takımla kararlaştırılmış teslimler değildir:

- Paylaşılacak CSV'nin dosya yolu, UTF-8 / BOM tercihi, ayırıcı ve alan şemasını birlikte belirlemek.
- Veri sözlüğünde tarih biçimi, sayısal alanlar, zorunlu alanlar ve kategori değerlerini tanımlamak; kişisel veri içermeyen sentetik veri kullanmak.
- Önce küçük bir örnek dosyayla okuma ve doğrulama denemesi yapmak; ardından üzerinde anlaşılan veri setini commit bağlantısıyla teslim etmek.

## PM raporunda kullanılabilecek olgusal satır

| Üye | Katkı | Referans |
| --- | --- | --- |
| Hiranur Doğan — BE | Sentetik veri teslimi, BE talimatlarının açıklanması, CSV doğrulama iyileştirmesi ve Grup D BE becerisinin çapraz incelemesi | Grup C [#12](https://github.com/MAKU-VBA-GBT-II/group-c/issues/12), [#18](https://github.com/MAKU-VBA-GBT-II/group-c/issues/18), [#25](https://github.com/MAKU-VBA-GBT-II/group-c/issues/25); Grup D [#25](https://github.com/MAKU-VBA-GBT-II/group-d/issues/25) |

**Araç ve kısa istem özeti:** Codex, PowerShell, Git ve GitHub REST API kullanıldı. İstem özeti: “Hiranur'un doğrulanmış teslimlerini kanıt bağlantılarıyla derle; yaşanan sorunu ve çözümünü belirt; sonraki dönem ile Görev 3 için öneriler hazırla.” Bu katkı kaydı takım KPI hesabı veya PM onayı yerine geçmez.

Kanıt: skills/pm-rapor/SKILL.md becerisini kullanarak Codex, PowerShell ve GitHub REST API ile ürettim.
