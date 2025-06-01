import pandas as pd

df = pd.read_excel("data_penjualan.xlsx")
print("5 baris pertama data:")
print(df.head())

df["Total Harga"] = df ["Jumlah"] * df["Harga Satuan"]
print("\nData dengan kolom Total Harga:")

elekrtonik = df[df["Kategori"] == "Elektronik"]
elekrtonik.to_excel("elektronik.xlsx", index=False)
print("\nData kategori Elektronik telah disimpan ke 'elektronik.xlsx'.")

rekap = df.groupby("Kategori")["Total Harga"].sum().reset_index()
rekap.columns = ["Kategori", "Total Pendapatan"]
print("\nReakap Pendaptan per Kategori:")
print(rekap)

df_sorted = df.sort_values(by="Total Harga", ascending=False)
df_sorted.to_excel("penjualan_terurut.xlsx", index=False)
print ("\ndata telah disimpan ke 'penjualan_terurut.xlsx' Berdasarkan total Harga")