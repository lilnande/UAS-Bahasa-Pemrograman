# Data barang akan disimpan dalam list
barang_list = []

def menu():
    print("\nPilih menu:")
    print("a. Input data barang")
    print("b. Tampilkan data barang")
    print("c. Hapus data barang")
    print("d. Mencari data barang")
    print("e. Hitung jumlah pembelian")
    print("f. Keluar")
    choice = input("Masukkan pilihan (a-f): ")
    return choice

def input_data_barang():
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    barang_list.append({"Nama": nama, "Harga": harga, "Stok": stok})
    print(f"Barang {nama} telah ditambahkan.")

def tampilkan_data_barang():
    if not barang_list:
        print("Tidak ada data barang.")
    else:
        for i, barang in enumerate(barang_list):
            print(f"{i+1}. Nama: {barang['Nama']}, Harga: {barang['Harga']}, Stok: {barang['Stok']}")

def hapus_data_barang():
    tampilkan_data_barang()
    if not barang_list:
        return
    nomor = int(input("Masukkan nomor barang yang akan dihapus: "))
    if 0 < nomor <= len(barang_list):
        barang_dihapus = barang_list.pop(nomor - 1)
        print(f"Barang {barang_dihapus['Nama']} telah dihapus.")
    else:
        print("Nomor tidak valid.")

def mencari_data_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    ditemukan = False
    for barang in barang_list:
        if barang["Nama"].lower() == nama.lower():
            print(f"Nama: {barang['Nama']}, Harga: {barang['Harga']}, Stok: {barang['Stok']}")
            ditemukan = True
            break
    if not ditemukan:
        print("Barang tidak ditemukan.")

def hitung_jumlah_pembelian():
    tampilkan_data_barang()
    if not barang_list:
        return
    nomor = int(input("Masukkan nomor barang yang akan dibeli: "))
    if 0 < nomor <= len(barang_list):
        jumlah = int(input("Masukkan jumlah pembelian: "))
        barang = barang_list[nomor - 1]
        if jumlah <= barang["Stok"]:
            total_harga = jumlah * barang["Harga"]
            barang["Stok"] -= jumlah
            print(f"Total harga: {total_harga}")
            print(f"Stok barang {barang['Nama']} sekarang: {barang['Stok']}")
        else:
            print("Stok tidak mencukupi.")
    else:
        print("Nomor tidak valid.")

def mainloop():
    while True:
        choice = menu()
        if choice == 'a':
            input_data_barang()
        elif choice == 'b':
            tampilkan_data_barang()
        elif choice == 'c':
            hapus_data_barang()
        elif choice == 'd':
            mencari_data_barang()
        elif choice == 'e':
            hitung_jumlah_pembelian()
        elif choice == 'f':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    mainloop()
