# Program Daftar Nilai Mahasiswa

# Dictionary untuk menyimpan data mahasiswa
mahasiswa = {}

def tambah_data():
    nama = input("Masukkan Nama Mahasiswa: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
    print("Data berhasil ditambahkan.")

def ubah_data():
    nama = input("Masukkan Nama Mahasiswa yang akan diubah: ")
    if nama in mahasiswa:
        tugas = float(input("Masukkan Nilai Tugas Baru: "))
        uts = float(input("Masukkan Nilai UTS Baru: "))
        uas = float(input("Masukkan Nilai UAS Baru: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        mahasiswa[nama] = {'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
        print("Data berhasil diubah.")
    else:
        print("Mahasiswa tidak ditemukan.")

def hapus_data():
    nama = input("Masukkan Nama Mahasiswa yang akan dihapus: ")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print("Data berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

def tampilkan_data():
    if mahasiswa:
        print("\nDaftar Nilai Mahasiswa:")
        print("Nama\t\tTugas\tUTS\tUAS\tNilai Akhir")
        for nama, nilai in mahasiswa.items():
            print(f"{nama}\t{nilai['tugas']}\t{nilai['uts']}\t{nilai['uas']}\t{nilai['nilai_akhir']:.2f}")
    else:
        print("Belum ada data mahasiswa.")

def cari_data():
    nama = input("Masukkan Nama Mahasiswa yang dicari: ")
    if nama in mahasiswa:
        print("\nData Nilai Mahasiswa:")
        print("Nama\t\tTugas\tUTS\tUAS\tNilai Akhir")
        nilai = mahasiswa[nama]
        print(f"{nama}\t{nilai['tugas']}\t{nilai['uts']}\t{nilai['uas']}\t{nilai['nilai_akhir']:.2f}")
    else:
        print("Mahasiswa tidak ditemukan.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu utama
menu()
