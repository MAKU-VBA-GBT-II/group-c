import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Proje klasorunden calistirilmalidir
veri_yolu = Path("data/banka-islemleri.csv")
cikti_klasoru = Path("visuals")
cikti_klasoru.mkdir(parents=True, exist_ok=True)

if not veri_yolu.exists():
    raise FileNotFoundError(f"Veri dosyasi bulunamadi: {veri_yolu}")

df = pd.read_csv(veri_yolu, encoding="utf-8-sig")

gerekli_sutunlar = {"tarih", "tutar", "musteri_segmenti"}
eksik = gerekli_sutunlar - set(df.columns)
if eksik:
    raise ValueError(f"Eksik sutunlar: {', '.join(sorted(eksik))}")

df["tarih"] = pd.to_datetime(df["tarih"], errors="coerce")
df["tutar"] = pd.to_numeric(df["tutar"], errors="coerce")

# Grafik 1: Gunluk toplam islem tutari
gunluk = (
    df.dropna(subset=["tarih", "tutar"])
    .groupby("tarih")["tutar"]
    .sum()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(gunluk.index, gunluk.values, marker="o", linewidth=2)
ax.set_title("Gunluk Toplam Islem Tutari")
ax.set_xlabel("Tarih")
ax.set_ylabel("Toplam islem tutari (TL)")
ax.grid(True, alpha=0.3)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(cikti_klasoru / "gunluk-islem-tutari.png", dpi=160)
plt.close(fig)

# Grafik 2: Musteri segmentine gore islem sayisi
segment = df["musteri_segmenti"].dropna().value_counts()

fig, ax = plt.subplots(figsize=(9, 6))
ax.bar(segment.index.astype(str), segment.values)
ax.set_title("Musteri Segmentine Gore Islem Sayisi")
ax.set_xlabel("Musteri segmenti")
ax.set_ylabel("Islem sayisi (adet)")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(cikti_klasoru / "musteri-segmenti.png", dpi=160)
plt.close(fig)

print("Grafikler basariyla olusturuldu:")
print(cikti_klasoru / "gunluk-islem-tutari.png")
print(cikti_klasoru / "musteri-segmenti.png")
