from prettytable import PrettyTable
class BarangMusik:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        self.terjual = 0  

    def __str__(self):
        return f"Barang: {self.nama}, Jumlah: {self.jumlah}, Harga: {self.harga}, Terjual: {self.terjual}"



class TokoAlatMusik:
    def __init__(self):
        self.inventaris = []

    def tambah_barang(self, barang):
        self.inventaris.append(barang)

    def tampilkan_inventaris(self):
        table = PrettyTable()
        table.field_names = ["Nama Barang", "Jumlah", "Harga"]
        for barang in self.inventaris:
            table.add_row([barang.nama, barang.jumlah, barang.harga])
            table.add_row([barang.nama, barang.jumlah, barang.harga])
        print(table)

    def perbarui_barang(self, nama_barang, jumlah_baru, harga_baru):
        for barang in self.inventaris:
            if barang.nama == nama_barang:
                barang.jumlah = jumlah_baru
                barang.harga = harga_baru
                print(f"Barang {nama_barang} berhasil diperbarui.")
                return
        print(f"Barang {nama_barang} tidak ditemukan dalam inventaris.")

    def hapus_barang(self, nama_barang):
        for barang in self.inventaris:
            if barang.nama == nama_barang:
                self.inventaris.remove(barang)
                print(f"Barang {nama_barang} berhasil dihapus.")
                return
        print(f"Barang {nama_barang} tidak ditemukan dalam inventaris.")


class Pengguna:
    def __init__(self, peran):
        self.peran = peran

    def login(self):
        password = input("Masukkan kata sandi: ")

        # password admin dan pembeli
        admin_password = "admin123"
        pembeli_password = "pembeli123"

        if self.peran == 'admin':
            if password == admin_password:
                print("Login berhasil!")
                self.menu_admin()
            else:
                print("Kata sandi salah. Coba lagi.")
        elif self.peran == 'pembeli':
            if password == pembeli_password:
                print("Login berhasil!")
                self.menu_pembeli()
            else:
                print("Kata sandi salah. Coba lagi.")


    def menu_admin(self):
        while True:
            print("\nMenu Admin:")
            print("1. Tambah Barang")
            print("2. Tampilkan Inventaris")
            print("3. Perbarui Barang")
            print("4. Hapus Barang")
            print("5. Keluar")
            pilihan = int(input("Masukkan pilihan Anda: "))

            if pilihan == 1:
                nama_barang = input("Masukkan nama barang: ")
                jumlah = int(input("Masukkan jumlah: "))
                harga = float(input("Masukkan harga: "))
                barang_musik = BarangMusik(nama_barang, jumlah, harga)
                toko_alat_musik.tambah_barang(barang_musik)
            elif pilihan == 2:
                toko_alat_musik.tampilkan_inventaris()
            elif pilihan == 3:
                nama_barang = input("Masukkan nama barang untuk diperbarui: ")
                jumlah_baru = int(input("Masukkan jumlah baru: "))
                harga_baru = float(input("Masukkan harga baru: "))
                toko_alat_musik.perbarui_barang(nama_barang, jumlah_baru, harga_baru)
            elif pilihan == 4:
                nama_barang = input("Masukkan nama barang untuk dihapus: ")
                toko_alat_musik.hapus_barang(nama_barang)
            elif pilihan == 5:
                break

    def menu_pembeli(self):
        while True:
            print("\nMenu Pembeli:")
            print("1. Tampilkan Inventaris")
            print("2. Transaksi")
            print("3. Keluar")
            pilihan = int(input("Masukkan pilihan Anda: "))

            if pilihan == 1:
                toko_alat_musik.tampilkan_inventaris()
            elif pilihan == 2:
                self.transaksi()
            elif pilihan == 3:
                break

    def transaksi(self):
        print("Daftar Barang:")
        toko_alat_musik.tampilkan_inventaris()
        nama_barang = input("Masukkan nama barang yang ingin Anda beli: ")
     
        barang = None
        for item in toko_alat_musik.inventaris:
            if item.nama == nama_barang:
                barang = item
                break

        if barang:
            quantity = int(input("Masukkan jumlah yang ingin Anda beli: "))

            
            if quantity > barang.jumlah:
                print("Stok tidak mencukupi.")
                return

            
            barang.jumlah -= quantity
            barang.terjual += quantity
            print(f"Transaksi berhasil! Anda telah membeli {quantity} {barang.nama}.")

        else:
            print(f"Barang {nama_barang} tidak ditemukan dalam inventaris.")


toko_alat_musik = TokoAlatMusik()

print("Selamat datang di Toko Alat Musik!")
while True:
    peran = input("Masukkan peran Anda (admin/pembeli), atau 'keluar' untuk keluar: ").lower()

    if peran == 'admin' or peran == 'pembeli':
        pengguna = Pengguna(peran)
        pengguna.login()
    elif peran == 'keluar':
        break
    else:
        print("Peran tidak valid. Harap masukkan 'admin', 'pembeli', atau 'keluar'.")
