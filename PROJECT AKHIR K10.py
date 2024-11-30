wisata_list = []

def add_tempat_wisata(tipe, nama, lokasi, deskripsi, kisaran_harga, rating):
    wisata = {
        "tipe" : tipe, 
        "nama" : nama,
        "lokasi" : lokasi,
        "deskripsi" : deskripsi,
        "kisaran HTM" : kisaran_harga,
        "rating" : rating
    }
    wisata_list.append(wisata)

add_tempat_wisata("Alam", "Gunung Bromo", "Jawa Timur", "Gunung berapi yang terkenal dengan pemandangan sunrise nya.", "50000-100000", 4.8)
add_tempat_wisata("Alam", "Pantai Kuta", "Bali", "Pantai yang terkenal dengan ombaknya yang cocok untuk berselancar.", "15000-50000", 4.0)
add_tempat_wisata("Alam", "Danau Toba", "Sumatera Utara", "Danau terbesar di Indonesia yang terletak di kawah gunung berapi.", "15000-50000", 3.6)
add_tempat_wisata("Budaya", "Candi Borobudur", "Jawa Tengah", "Candi terbesar di Indonesia yang merupakan warisan dunia.", "50000-100000", 4.7)
add_tempat_wisata("Budaya", "Taman Mini Indonesia Indah", "Jakarta", "Taman yang menampilkan budaya dan keanekaragaman Indonesia.", "15000-50000", 3.9)

def tampilkan_tempat_wisata(apa):
    if not wisata_list:
        print(f"\n--- Daftar Wisata {apa} tidak ditemukan !! ---\n")
        return

    elif wisata_list:
        cek_wisata = [wisata for wisata in wisata_list if
                       apa.lower() == wisata["tipe"].lower()]

        if not cek_wisata:
            print(f"\n--- Daftar Wisata {apa} tidak ditemukan !! ---\n")
            return
        
        elif cek_wisata:
            print(f"\n==== Daftar Tempat Wisata {apa} ====")
            for wisata in cek_wisata:
                print(f"Tipe Wisata        : {wisata['tipe']}")
                print(f"Nama Tempat Wisata : {wisata['nama']}")
                print(f"Lokasi Wisata      : {wisata['lokasi']}")
                print(f"Deskripsi wisata   : {wisata['deskripsi']}")
                print(f"kisaran HTM        : Rp{wisata['kisaran HTM']}")
                print(f"Rating             : {wisata['rating']}/5")
                print("----")

def update_tempat_wisata(nama):
    for wisata in wisata_list:
        if wisata['nama'].lower() == nama.lower():
            print(f"\n--- Memperbarui informasi Wisata {nama} ---")
            lokasi_new = input("Lokasi baru : ")
            deskripsi_new = input("Deskripsi baru : ")
            kisaran_harga_new = input("Kisaran HTM baru : ")
            rating = float(input("Rating Wisata baru (1-5) : "))
            rating = cek_rating(rating)
            wisata['lokasi'] = lokasi_new
            wisata['deskripsi'] = deskripsi_new
            wisata['kisaran HTM'] = kisaran_harga_new
            wisata['rating'] = rating
            print(f"--- Informasi Wisata {nama} telah diperbarui !! ---\n")
            break
    else:
        print(f"\n--- Tempat Wisata {nama} tidak ditemukan !! ---\n")

def delete_tempat_wisata(nama):
    for i in range(len(wisata_list)):
        wisata = wisata_list[i]
        if wisata['nama'].lower() == nama.lower():
            del wisata_list[i]
            print(f"\n--- Tempat Wisata {nama} telah dihapus! ---\n")
            break
    else:
        print(f"\n--- Tempat Wisata {nama} tidak ditemukan !! ---\n")

def cek_rating(rating):
    while True:
        if 1 <= rating <= 5:
            return rating
        elif rating > 5:
            print("--- Rating diantara 1 s/d 5 !! --- ")
            rating = float(input("Rating Wisata (1-5) : "))

def rekomenHTM(wisata_list, jawab):
    rekom = [wisata for wisata in wisata_list if
                jawab in wisata['kisaran HTM']]
    return rekom

def rekomenRating(rating_min, rating_max):
    rekomendasi = [wisata for wisata in wisata_list if 
                    rating_min <= wisata['rating'] <= rating_max]
    return rekomendasi

def menu():
    while True:
        print("========================================")
        print(" Informasi Berbagai Macam Tempat Wisata ")
        print("========================================")
        print("1. Menampilkan Informasi tempat wisata")
        print("2. Tambah tempat wisata Alam")
        print("3. Tambah tempat wisata Budaya")
        print("4. Update informasi tempat wisata")
        print("5. Delete informasi tempat wisata")
        print("6. Rekomendasi tempat wisata")
        print("7. Keluar")
        print("========================================")

        ask = int(input("Pilih menu [1/2/3/4/5/6/7] : "))
        print("========================================")

        if ask == 1:
            apa = input("Ingin menampilkan Tipe Daftar Wisata apa [Alam/Budaya] : ")
            tampilkan_tempat_wisata(apa)

        elif ask == 2:
            tipe = "Alam"
            print("\n--- Tambahkan Wisata Alam ---")
            print(f"Tipe Wisata : {tipe}")
            nama = input("Nama Tempat Wisata : ")
            lokasi = input("Lokasi : ")
            deskripsi = input("Deskripsi : ")
            kisaran_harga = input("Kisaran HTM : ")
            rating = float(input("Rating Wisata (1-5) : "))
            rating = cek_rating(rating)
            add_tempat_wisata(tipe, nama, lokasi, deskripsi, kisaran_harga, rating)
            print(f"--- Tempat Wisata {nama} Berhasil ditambahkan !! ---\n")

        elif ask == 3:
            tipe = "Budaya"
            print("\n--- Tambahkan Wisata Budaya ---")
            print(f"Tipe Wisata : {tipe}")
            nama = input("Nama Tempat Wisata : ")
            lokasi = input("Lokasi : ")
            deskripsi = input("Deskripsi : ")
            kisaran_harga = input("kisaran HTM : ")
            rating = float(input("Rating Wisata (1-5) : "))
            rating = cek_rating(rating)
            add_tempat_wisata(tipe, nama, lokasi, deskripsi, kisaran_harga, rating)
            print(f"--- Tempat Wisata {nama} Berhasil ditambahkan !! ---\n")

        elif ask == 4:
            nama = input("Masukkan nama tempat wisata yang ingin diperbarui: ")
            update_tempat_wisata(nama)

        elif ask == 5:
            nama = input("Masukkan nama tempat wisata yang ingin dihapus: ")
            delete_tempat_wisata(nama)
        
        elif ask == 6:
            print("\n------  Rekomendasi Wisata  ------")
            print("1. Ingin HTM Terjangkau")
            print("2. Ingin Rating Tertinggi/Terendah")
            pilih = int(input("Pilih rekomendasi [1/2] : "))
            print("-----------------------------------")
            
            if not wisata_list:               
                print(f"\n--- Daftar Wisata dengan rekomendasi yang diinginkan tidak ditemukan !! ---\n")

            elif wisata_list:
                if pilih == 1:
                    print("\n------ Pilih Mau Kisaran Berapa ------")
                    print("1. Kisaran HTM Rp0-50000")
                    print("2. Kisaran HTM Rp50000-100000")
                    print("----------------------------------------")
                    jawab = input("[15000-50000 / 50000-100000] : ")
                    print("----------------------------------------")

                    rekomendasi = rekomenHTM(wisata_list, jawab)
                    if rekomendasi:
                        print(f"\n==== Daftar Tempat Wisata dengan HTM Rp{jawab} ====")
                        for wisata in rekomendasi:
                            print(f"Tipe Wisata        : {wisata['tipe']}")
                            print(f"Nama Tempat Wisata : {wisata['nama']}")
                            print(f"Lokasi Wisata      : {wisata['lokasi']}")
                            print(f"Deskripsi wisata   : {wisata['deskripsi']}")
                            print(f"kisaran HTM        : Rp{wisata['kisaran HTM']}")
                            print(f"Rating             : {wisata['rating']}/5")
                            print("----")
                    elif not rekomendasi:
                        print(f"\n--- Tempat Wisata dengan HTM yang diinginkan tidak ditemukan !! ---\n")

                elif pilih == 2:
                    print("\n------ Pilih Mau Rekomendasi Rating Berapa ------")
                    print("1. Rating antara 1-3")
                    print("2. Rating antara 3.1-4")
                    print("3. Rating antara 4.1-5")
                    print("----------------------------------------")
                    rat = int(input("Pilih [1/2/3] : "))
                    print("----------------------------------------")

                    if rat == 1:
                        rekomendasi = rekomenRating(1, 3)
                    elif rat == 2:
                        rekomendasi = rekomenRating(3.1, 4)
                    elif rat == 3:
                        rekomendasi = rekomenRating(4.1, 5)
                    else:
                        print("\n--- Maaf Inputan Anda Invalid !! ---\n")
                        continue

                    if rekomendasi:
                        print(f"\n==== Daftar Tempat Wisata Rekomendasi Rating ====")
                        for wisata in rekomendasi:
                            print(f"Tipe Wisata        : {wisata['tipe']}")
                            print(f"Nama Tempat Wisata : {wisata['nama']}")
                            print(f"Lokasi Wisata      : {wisata['lokasi']}")
                            print(f"Deskripsi wisata   : {wisata['deskripsi']}")
                            print(f"kisaran HTM        : Rp{wisata['kisaran HTM']}")
                            print(f"Rating             : {wisata['rating']}/5")
                            print("----")
                    elif not rekomendasi:
                        print(f"\n--- Tempat Wisata dengan rating yang diinginkan tidak ditemukan !! ---\n")                        
                elif pilih > 2:
                    print("\n--- Maaf Inputan Anda Invalid !! ---\n")  

        elif ask == 7:
            print("\n==== Program telah selesai !! ====")
            print("====      Terima kasih !!     ====\n")
            break 

menu()