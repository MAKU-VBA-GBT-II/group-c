# Görev 3 — Veri Değişimi (Data Exchange)

Bu klasör, **Grup C (Bankacılık)** ile partner takım **Grup D (Müşteri Hizmetleri / Çağrı Merkezi)** arasındaki veri değişim dosyasını içerir.

## Paylaşılan Veri Dosyası: `output.csv`

- **Sektör:** Bankacılık
- **Kaynak:** `data/banka-islemleri.csv`
- **Dosya Yolu:** `exchange/output.csv`
- **Karakter Kodlaması:** UTF-8 (BOM'lu, `utf-8-sig`)
- **Kayıt Sayısı:** 500 satır (başlık ile birlikte 501 satır)
- **Sütun Sayısı:** 10
- **Ayırıcı:** Virgül (`,`)

### Sütun Şeması ve Tanımları

| Sütun Adı | Veri Türü | Zorunlu | Açıklama | Örnek Değer |
|---|---|---|---|---|
| `islem_id` | Tamsayı | Evet | Benzersiz işlem numarası (1001-1500) | `1001` |
| `tarih` | Tarih (ISO 8601) | Evet | İşlem tarihi (YYYY-MM-DD, 2026-01-01 / 2026-09-30) | `2026-04-15` |
| `musteri_id` | Tamsayı | Evet | Müşteri kimlik numarası (10001-10100) | `10042` |
| `islem_turu` | Metin | Evet | 7 farklı bankacılık işlem türü | `Havale`, `EFT`, `Fatura ödeme` |
| `tutar` | Ondalık Sayı | Evet | İşlem tutarı (TL, iki basamak ondalık) | `1250.50` |
| `kanal` | Metin | Evet | İşlem kanalı | `Mobil bankacılık`, `ATM`, `Şube` |
| `sehir` | Metin | Evet | Müşteri/işlem şehri (6 şehir) | `İstanbul`, `Ankara`, `Burdur` |
| `durum` | Metin | Evet | İşlemin nihai durumu | `Başarılı`, `Başarısız`, `Beklemede` |
| `musteri_segmenti` | Metin | Evet | Müşteri segmenti | `Bireysel`, `Ticari`, `Kurumsal` |
| `islem_suresi_sn` | Tamsayı | Evet | İşlem tamamlanma süresi (saniye) | `45` |

## Entegrasyon Notları (Grup D İçin)

1. `musteri_id` alanı üzerinden Grup D'nin müşteri talep/çağrı kayıtları ile bankacılık işlemleri eşleştirilebilir.
2. Dosya `utf-8-sig` kodlamasındadır; Pandas veya Python standart `csv` kütüphanesiyle okunurken `encoding='utf-8-sig'` parametresi kullanılmalıdır.
