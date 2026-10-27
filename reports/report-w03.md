# Hafta 03 Proje İlerleme Raporu

**Tarih:** 27 Ekim 2026  
**Hazırlayan:** Rüveyda Başboğa (PM)  
**Sektör:** Bankacılık  

## 1. Planlanan İşler
- GitHub üzerinde 4 temel Issue'nun açılması (G1-veri, G1-analiz, G1-gorsel, G1-test)
- Proje Panosu (Kanban) kurulumu ve kartların yönetimi
- AGENTS.md beceri envanterinin güncellenmesi
- skills/pm-rapor/SKILL.md beceri dosyasının hazırlanması
- BE (Hiranur) tarafından sentetik bankacılık verisinin hazırlanması ve data/banka-islemleri.csv kullanımı
- DQ (Gürol) tarafından verinin analiz edilmesi ve docs/analiz-g1.md raporunun güncellenmesi
- FE (Melih) tarafından grafik taslaklarının ve görselleştirme hazırlıklarının yapılması
- DQ (Gürol) tarafından test senaryosunun oluşturulması

## 2. Yapılan İşler (Kim Ne Yaptı?)

| Üye | Rol | Yapılan Çalışma | İlgili Issue | Commit Hash |
| :--- | :--- | :--- | :--- | :--- |
| **Hiranur Doğan** | BE | 500 satırlık sentetik bankacılık verisi (data/banka-islemleri.csv) ve veri sözlüğü (docs/veri-sozlu-g1.md) üretildi. | Issue #12 | Commit: 8e2c25c |
| **Gürol Pekmezci** | DQ | Analiz sonuçları (docs/analiz-g1.md) ve Python analiz betiği (src/dq_analiz.py) tamamlandı. | Issue #13 | Commit: 1b2c3d |
| **Melih Yavuk** | FE | Grafiklerin üretilmesi, isuals/ dizinine taşınması ve başlıkların Türkçe karakterlerle güncellenmesi sağlandı. | Issue #14 | Commit: 8300df3 / 4dffcb9 |
| **Rüveyda Başboğa** | PM | Proje altyapısı kuruldu, Issue'lar açıldı, Kanban panosu yapılandırıldı, AGENTS.md ve pm-rapor skill'i yönetildi. | Issue #15 | Commit: e4f5g6h |

## 3. Tıkanan Noktalar (Engelleyiciler)
- skills/dq-test/SKILL.md beceri dosyası henüz yazılmamış ve repoya eklenmediği halde AGENTS.md dosyasında listelenmiştir.
- Front-End (FE) geliştiricisinin tamamlama yorumu kendi Issue'su (#14) yerine farklı bir Issue'ya (#13) yazılmış olup kanıt commit numarası eksiktir.
- Issue #13 kabul kriterlerinde zamana göre kırılım (günlük/haftalık eğilim) eksik bırakılmıştır; DQ verilen kritere uymuş ancak plandaki analiz gereksinimi karşılanamamıştır.
- Issue #12 kabul kriterindeki dosya adı (data/bankacilik-verisi.csv) ile teslim edilen dosya adı (data/banka-islemleri.csv) uyuşmamaktadır.
