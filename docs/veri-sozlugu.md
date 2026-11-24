# VBA BANKACILIK — Veri Sözlüğü (Duyuru 10 Güncel)

Bu doküman, Çok Ajanlı Şirket Programı (Duyuru 10) kapsamında dış piyasa verileriyle (TCMB Döviz Kurları ve KAP Bildirimleri) eşleştirilmek üzere genişletilen `data/banka-islemleri.csv` veri setinin alan tanımlarını içerir.

---

## Veri Seti Özeti

* **Dosya Yolu:** `data/banka-islemleri.csv`
* **Üretici Betik:** `src/banka_veri_uret.py`
* **Kayıt Sayısı:** 500 (Dışarıdan `--kayit-sayisi` parametresiyle dinamik değiştirilebilir)
* **Tarih Kapsamı:** 2026-10-01 ile 2026-11-20 arası (Dışarıdan `--baslangic` ve `--bitis` ile ayarlanabilir)
* **Para Birimleri:** TRY, USD, EUR (Dışarıdan `--doviz-listesi` ile ayarlanabilir)

---

## Alan Tanımları

| Sütun Adı | Veri Tipi | Zorunlu mu? | Açıklama | Örnek Değerler | Dış Veri Eşleşmesi (TCMB / KAP) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `islem_id` | Integer | Evet | İşlemin benzersiz kimlik numarası | `1001`, `1042` | İç sistem referansı |
| `tarih` | Date (YYYY-MM-DD) | Evet | Finansal işlemin gerçekleştiği gün | `2026-10-16`, `2026-11-02` | **TCMB & KAP:** Günlük bülten ve bildirim tarihi ile birebir eşleşir |
| `islem_saati` | Time (HH:MM:SS) | Evet | İşlemin gerçekleştiği saat, dakika, saniye | `09:54:11`, `14:42:37` | **KAP:** Kamuyu aydınlatma bildirim saati ve seans içi kur sıçramalarıyla eşleşir |
| `musteri_id` | Integer | Evet | İşlemi yapan müşterinin tekil numarası (10001–10100) | `10043`, `10057` | Müşteri işlem sıklığı ve profil analizi |
| `musteri_segmenti` | String | Evet | Müşterinin bankacılık kategorisi | `Bireysel`, `Ticari`, `Kurumsal` | Limit ve olağan hacim kontrolleri |
| `islem_turu` | String | Evet | Gerçekleştirilen bankacılık işleminin çeşidi | `Havale`, `EFT`, `Döviz Alımı`, `Döviz Satımı`, `Yurtdışı Para Transferi (SWIFT)`, `Para Çekme`, `Para Yatırma` | **Piyasa Korelasyonu:** Kur artışlarında döviz alım/satım veya SWIFT eğilimleri izlenir |
| `doviz_cinsi` | String | Evet | İşlemin yapıldığı para birimi kodu (ISO 4217) | `TRY`, `USD`, `EUR` | **TCMB:** TCMB XML kurlarındaki para birimleri ile eşleşir |
| `tutar` | Float | Evet | İşlemin orijinal para birimindeki nominal tutarı | `14204.72`, `279148.09` | Hacim anomalisi kontrolü |
| `kur_degeri` | Float | Evet | İşlem tarihindeki referans döviz kuru (TRY için 1.0) | `34.8467`, `37.2105`, `1.0` | **TCMB:** TCMB gösterge kur değeri |
| `islem_tutari_try` | Float | Evet | İşlem tutarının Türk Lirası cinsinden brüt karşılığı (`tutar * kur_degeri`) | `494987.62`, `9727473.49` | MASAK / AML şüpheli işlem parasal eşik denetimi |
| `kanal` | String | Evet | İşlemin gerçekleştirildiği bankacılık kanalı | `Mobil bankacılık`, `İnternet bankacılığı`, `Şube`, `ATM` | Kanal bazlı risk analizi |
| `sehir` | String | Evet | Müşterinin kayıtlı olduğu / işlemin yapıldığı il | `İstanbul`, `Ankara`, `İzmir`, `Antalya`, `Bursa`, `Burdur` | Coğrafi dağılım |
| `durum` | String | Evet | Banka sistemindeki anlık işlem sonucu | `Başarılı`, `Şüpheli/Beklemede`, `Başarısız` | Ajan 3'ün denetleyeceği hedef durum |
| `islem_suresi_sn` | Integer | Evet | İşlemin tamamlanma süresi (saniye) | `45`, `180` | Dijital ve şube kanalı hız doğrulama |
| `islem_aciklamasi` | String | Evet | İşleme ait açıklama ve gerekçe metni | `İthalat faturası döviz temini`, `Şirket içi hesap aktarımı`, `Piyasa kapanışı sonrası yüksek EFT` | **KAP:** Şirket olaylarıyla (temettü, sermaye artırımı, ithalat) anlamsal doğrulama |

---

## Simülasyon Çalıştırma Komutları

Duyuru 10 gereği simülasyon betiği dışarıdan parametre ve aralık kabul etmektedir:

```bash
# Varsayılan üretim (500 kayıt, 1.000 TL - 500.000 TL, TRY/USD/EUR)
python src/banka_veri_uret.py

# Özel parametrelerle üretim (Grup kararı)
python src/banka_veri_uret.py --kayit-sayisi 500 --min-tutar 1000 --max-tutar 500000 --doviz-listesi USD,EUR,TRY

# Tarih aralığı ve özel dosya yoluyla üretim
python src/banka_veri_uret.py --baslangic 2026-10-01 --bitis 2026-11-20 --cikti data/banka-islemleri.csv
```
