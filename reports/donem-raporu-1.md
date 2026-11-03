# Dönem Raporu 1 (Group C)

**Tarih:** 2026-11-08
**Raporlayan (PM):** Rüveyda Başboğa
**Takım:** Group C (Hiranur Doğan - BE, Melih Yavuk - FE, Gürol Pekmezci - DQ, Elanur Ekim - Junior)

## 1. Yönetici Özeti
Group C, Görev 1 ve Görev 2 süreçlerinde bankacılık veri analizi pipelinesı, sentetik veri üretimi ve BE/DQ/FE altyapı çalışmalarını tamamlamıştır.

## 2. Teslim Edilenler
- **Sentetik Veri & BE Altyapısı:** Sabit seed=42 ile 500 kayıtlı sentetik bankacılık verisi, veri sözlüğü ve CSV doğrulama geliştirmeleri (#12, #18, #25).
- **Çapraz İnceleme:** Grup D'nin be-veri becerisi çapraz incelemesi (Grup D #25).
- **Sprint Raporları:** Hafta 3 ve Hafta 5 sprint raporları (report-w03.md, report-w05.md).

## 3. Sayılarla Dönem (Süreç KPI'ları)
| Üye | Rol | Commit Sayısı |
| :--- | :--- | :--- |
| Rüveyda Başboğa | PM | 19 |
| Hiranur Doğan | BE | 15 |
| Gürol Pekmezci | DQ | 6 |
| Melih Yavuk | FE | 4 |

## 4. Tıkananlar ve Çözümler
- **CoastSnap Rapor Yansıma Sorunu:** Yerelde güncellenen CoastSnap raporunun GitHub'da görünmemesi sorunu, sadece ilgili rapor güncellemesinin güncel main üzerine alınıp 004419c commit'i ile gönderilmesiyle çözüldü.
- **Git Çakışmaları:** Rapor güncellemelerinde yaşanan rebase ve branch çakışmaları git reset / checkout adımlarıyla aşıldı.

## 5. Kim Ne Yaptı
- **Rüveyda Başboğa (PM):** Sprint raporlama süreçlerini yönetti (report-w05.md) ve takım içi koordinasyonu sağladı (19 commit).
- **Hiranur Doğan (BE):** Sentetik bankacılık verisi teslimi (#12), BE çalıştırma talimatları (#18), CSV doğrulama iyileştirmesi (#25) ve Grup D BE becerisi çapraz incelemesini gerçekleştirdi (15 commit).
- **Gürol Pekmezci (DQ):** DQ veri analizi ve test dokümantasyonunu geliştirdi (6 commit).
- **Melih Yavuk (FE):** Prova verileri ve FE bileşenlerini hazırladı (4 commit).

## 6. Dersler
- Her teslimden sonra GitHub'daki dosya ve commit bağlantısını kontrol ederek aynı gün ilgili Issue'ya kanıt yorumu eklemek.
- Yerel çalışmalarda çakışma yaşamamak için git pull --rebase kullanımını alışkanlık haline getirmek.

## 7. Görev 3 Hazırlığı
- Group D ile veri değişimi öncesi CSV formatı, UTF-8/BOM tercihi, ayırıcı ve alan şemasını önceden yazılı olarak netleştirmek.
- Önce küçük bir örnek dosyayla doğrulama denemesi yapmak.
