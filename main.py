import re
from Data.Data1 import Data_Pendaftaran
from View.View1 import view_pendaftaran
from Process.Process1 import process_pendaftaran

def main():
    data_table = []  # Tempat menyimpan data pendaftaran
    while True:
        print("\nselamat datang!!!")
        print("Menu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Edit Data")
        print("4. Lihat Semua Data")
        print("5. Keluar")
        
        menu_choice = input("Pilih menu (1-5): ")
        
        if menu_choice == "1":
            # Tambah Data
            try:
                name, nim, phone, email = view_pendaftaran.get_input()
                data = Data_Pendaftaran(name, nim, phone, email)

                # Validasi data
                process_pendaftaran.validate_data(data)

                # Tambahkan data ke tabel
                data_table.append(data)
                view_pendaftaran.display_message("Pendaftaran berhasil dan valid!")
            except ValueError as e:
                view_pendaftaran.display_message(f"Error: {e}")

        elif menu_choice == "2":
            # Hapus Data
            if not data_table:
                view_pendaftaran.display_message("Tidak ada data untuk dihapus.")
            else:
                view_pendaftaran.table_view(data_table)
                try:
                    row_to_delete = int(input("Masukkan nomor data yang ingin dihapus: "))
                    if 1 <= row_to_delete <= len(data_table):
                        deleted_data = data_table.pop(row_to_delete - 1)
                        view_pendaftaran.display_message(f"Data '{deleted_data.name}' berhasil dihapus.")
                    else:
                        view_pendaftaran.display_message("Nomor yang dimasukkan tidak valid.")
                except ValueError:
                    view_pendaftaran.display_message("Input harus berupa angka.")

        elif menu_choice == "3":
            # Edit Data
            if not data_table:
                view_pendaftaran.display_message("Tidak ada data untuk diedit.")
            else:
                view_pendaftaran.table_view(data_table)
                try:
                    row_to_edit = int(input("Masukkan nomor data yang ingin diedit: "))
                    if 1 <= row_to_edit <= len(data_table):
                        data = data_table[row_to_edit - 1]
                        print(f"Edit data untuk: {data.name}")
                        name = input(f"Nama ({data.name}): ") or data.name
                        nim = input(f"NIM ({data.nim}): ") or data.nim
                        phone = input(f"Nomor Telepon ({data.phone}): ") or data.phone
                        email = input(f"Email ({data.email}): ") or data.email

                        updated_data = Data_Pendaftaran(name, nim, phone, email)
                        process_pendaftaran.validate_data(updated_data)

                        data_table[row_to_edit - 1] = updated_data
                        view_pendaftaran.display_message(f"Data berhasil diperbarui untuk: {name}")
                    else:
                        view_pendaftaran.display_message("Nomor yang dimasukkan tidak valid.")
                except ValueError as e:
                    view_pendaftaran.display_message(f"Error: {e}")
                except Exception:
                    view_pendaftaran.display_message("Terjadi kesalahan saat mengedit data.")

        elif menu_choice == "4":
            # Lihat Semua Data
            if not data_table:
                view_pendaftaran.display_message("Belum ada data yang terdaftar.")
            else:
                view_pendaftaran.table_view(data_table)

        elif menu_choice == "5":
            # Keluar
            print("Terima kasih telah mendaftar!!!")
            break
        else:
            view_pendaftaran.display_message("Pilihan menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
