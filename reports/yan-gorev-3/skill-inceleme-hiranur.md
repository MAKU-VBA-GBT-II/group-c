# Yan Görev 3 — Çapraz Skill İncelemesi

**Issue başlığı:** Skill incelemesi: be-veri (Hiranur Doğan, Grup C)

**Hedef repo:** https://github.com/MAKU-VBA-GBT-II/group-d

**İstenen etiket:** `enhancement` — GitHub üzerinde eklendiği doğrulandı.

**Yayımlanan Issue:** https://github.com/MAKU-VBA-GBT-II/group-d/issues/25

**Durum:** Tamamlandı. Gerekçeli yanıt, etiket ve önerinin uygulandığı commit doğrulandı. Issue GitHub üzerinde açık; duyuruda kapatma şartı bulunmuyor.

## Son kontrol — 27 Ekim 2026

- Beceri sahibi `emin-emek`, [26 Ekim tarihli yanıtında](https://github.com/MAKU-VBA-GBT-II/group-d/issues/25#issuecomment-6422245630) öneriye katıldığını belirtmiş; göreli yolun yanlış klasöre çözülmesini gerekçe göstermiştir.
- Issue üzerinde `enhancement` etiketi bulunmaktadır.
- Öneri [ca87195 commit'inde](https://github.com/MAKU-VBA-GBT-II/group-d/commit/ca8719563f3410ad3fff437db21e7eff2c55808e) uygulanmıştır. Commit mesajı: `fix: SKILL.md veri-sozlugu link yolu duzeltildi (#25)`.
- Commit farkında `skills/be-veri/SKILL.md` içindeki bağlantının `../docs/veri-sozlugu-g1.md` yerine `../../docs/veri-sozlugu-g1.md` olarak değiştiği ve aynı sürümde hedef `docs/veri-sozlugu-g1.md` dosyasının bulunduğu GitHub API üzerinden doğrulanmıştır.

Kanıt: skills/be-veri/SKILL.md becerisini kullanarak PowerShell ve GitHub REST API ile kontrol kaydını ürettim.

---

Merhaba Emin,

Duyuru 5 / Yan Görev 3 kapsamında Grup C BE üyesi Hiranur Doğan olarak `be-veri` skill'inizi, üretim betiğinizi ve CSV çıktınızı inceledim.

**İncelenen sürüm:** [`b4296d3`](https://github.com/MAKU-VBA-GBT-II/group-d/commit/b4296d342cd58075461a70621cee39c6fc143ddf). Bulgular bu sürüm içindir.

## 1. Güçlü yan

[Skill'in 17–37. satırlarında](https://github.com/MAKU-VBA-GBT-II/group-d/blob/b4296d342cd58075461a70621cee39c6fc143ddf/skills/be-veri/SKILL.md#L17-L37) çalıştırma komutu, çıktı yolu, kodlama, kayıt/alan sayıları ve sabit tohum açıkça belirtilmiş. [65–68. satırlardaki](https://github.com/MAKU-VBA-GBT-II/group-d/blob/b4296d342cd58075461a70621cee39c6fc143ddf/skills/be-veri/SKILL.md#L65-L68) Python sürümü ve ek paket gerekmediği bilgisi de kurulumu kolaylaştırıyor. Betiği geçici bir klasörde iki ayrı süreçte çalıştırdım; iki çalıştırmanın çıktısı bayt düzeyinde aynıydı. Üretilen CSV'de ve repodaki CSV'de 200 veri kaydı, 9 alan ve 6 talep türü bulunduğunu doğruladım.

## 2. Eksik

[Skill'in 41. satırındaki](https://github.com/MAKU-VBA-GBT-II/group-d/blob/b4296d342cd58075461a70621cee39c6fc143ddf/skills/be-veri/SKILL.md#L41) veri sözlüğü bağlantısının göreli hedefi `../docs/veri-sozlugu-g1.md`. Dosya `skills/be-veri/` altında olduğundan bu bağlantı `skills/docs/veri-sozlugu-g1.md` yoluna çözülüyor; incelenen sürümde böyle bir dosya yok. Gerçek veri sözlüğü repo kökündeki `docs/veri-sozlugu-g1.md` dosyasında bulunuyor. Bu nedenle skill üzerinden şemaya gitmek isteyen okuyucu veya bağlantıyı izleyen ajan doğru dosyaya ulaşamıyor.

## 3. Somut öneri

41. satırdaki Markdown bağlantısını iki üst klasöre çıkacak şekilde düzeltmenizi öneriyorum:

```markdown
Detaylı alan tanımları ve kategorik değerler için bkz. [`docs/veri-sozlugu-g1.md`](../../docs/veri-sozlugu-g1.md).
```

Düzeltme sonrasında GitHub'da skill dosyasını açıp bağlantıya tıklayarak `docs/veri-sozlugu-g1.md` sayfasının açıldığını kontrol edebilirsiniz. Böylece mevcut üretim komutu ve şema arasındaki bağlantı tamamlanmış olur.

Duyuru gereği öneriye katılıp katılmadığınızı nedeninizle birlikte bu Issue altında yanıtlayabilir misiniz? Öneriyi uygularsanız düzeltme commit mesajında bu Issue'nun numarasını belirtmeniz yeterli.

**İnceleme aracı:** Codex. Bu değerlendirme, mevcut veri hatası kayıtlarından ayrı olarak skill'in şemaya yönlendirmesini ele alır.

**Etiket notu (ilk yayın):** İnceleme yayımlanırken yetki nedeniyle `enhancement` etiketi eklenememişti. Son kontrolde etiketin eklendiği doğrulandı.
