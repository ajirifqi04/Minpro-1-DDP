peralatan = ["Tenda", "Sleeping Bag", "Kompor Portable", "Tas Besar", "Jaket Gunung"]

while True:
    print("Sistem Manajemen Peralatan Mendaki Gunung")
    print("1. Menampilkan Daftar List Peralatan")
    print("2. Menambah Peralatan")
    print("3. Menghapus Peralatan")
    print("4. Keluar")

    pilihan = input("Pilih Menu (1-4): ")

    if pilihan == "1":
        print("Daftar Peralatan Mendaki:")
        print("1.", peralatan[0])
        print("2.", peralatan[1])
        print("3.", peralatan[2])
        print("4.", peralatan[3])
        print("5.", peralatan[4])

    elif pilihan == "2":
        tambah = input("Masukkan nama peralatan yang ingin ditambahkan: ")
        peralatan.append(tambah)
        print("Peralatan berhasil ditambahkan.")
        print("Daftar peralatan:", peralatan)

    elif pilihan == "3":
        hapus = input("Masukkan nama peralatan yang ingin dihapus: ")
        if hapus in peralatan:
            peralatan.remove(hapus)
            print(hapus, "berhasil dihapus.")
            print("Daftar peralatan sekarang:", peralatan)
        else:
            print("Peralatan tidak ditemukan.")

    elif pilihan == "4":
        print("Program Selesai.")
        break

    else:
        print("Pilihan tidak valid.")
