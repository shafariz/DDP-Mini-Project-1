print("#login")

nama = (input("Masukkan nama:"))
nim = (input("Masukkan nim:"))
prodi = (input("Masukkan prodi:"))

print("Selamat datang", nama)
print("NIM anda", nim)
print("Program studi anda", prodi)

print("# program menghitung gaji karyawan")

while True:
    jamkerja = int(input("Masukkan jam kerja:"))
    tarifkerja = float(input("Masukkan tarif kerja:"))

    if (jamkerja > 160) :
        tarifbonus = (tarifkerja + (tarifkerja * 0.1))
        print("tarif asli:", tarifkerja)
        print("tarif bonus:", tarifbonus)
    else:
        print("tarif asli:", tarifkerja)
        print("tidak mendapatkan bonus")

    keluar = input("apakah anda ingin keluar dari program? (yes/no):")
    if keluar == "yes" :
        print("terimakasih telah menggunakan program kami")
        break

