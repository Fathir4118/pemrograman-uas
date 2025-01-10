NAMA : MUHAMMAD FATHIR NURCHOLIS

NIM : 312410287

KELAS : TI.24.A.4

MATKUL : BAHASA PEMROGRAMAN

# PROJECT UAS

![tugasnya](https://github.com/user-attachments/assets/39dced2c-ed27-4053-a6ea-75618c84ca7b)

# |CLASS Data_Pendaftaran|

python


Berfungsi untuk merepresentasikan data mahasiswa.

Attributes:

`nama` = Nama Asli Peserta

`nim` = Nomor Induk Mahasiswa (NIM)

`phone` = Nomor Telphone Peserta

`email` = Email Peserta


# |class process_pendaftaran|

Memastikan semua data yang dimasukkan pengguna valid sebelum disimpan.

Validasi Tiap Atribut:

`validate_name:` Nama hanya boleh mengandung huruf (menggunakan .isalpha()).

`validate_nim:` NIM hanya boleh angka (menggunakan .isdigit()).

`validate_phone:` Nomor telepon hanya boleh angka.

`validate_email:` Email harus sesuai format yang valid (dengan regex).

`validate_data:` Memanggil semua fungsi validasi untuk memastikan semua atribut dalam sebuah objek valid.


# |Class view_pendaftaran|

Menyediakan antarmuka untuk input dan output data.

`get_input:` Mengambil input pengguna untuk nama, NIM, nomor telepon, dan email.

`table_view:` Menampilkan semua data dalam format tabel yang rapi. Setiap entri memiliki nomor urut.

`display_message:` Menampilkan pesan (contohnya error atau sukses) ke layar.


# |Fungsi main()|

Penjelasan Menu:

Tambah Data (Menu 1):

Mengambil input data pengguna.

Validasi data dilakukan sebelum ditambahkan ke data_table.

Hapus Data `(Menu 2)`:

Menampilkan tabel data.

Menghapus entri berdasarkan nomor yang dipilih pengguna.

Edit Data `(Menu 3)`:

Menampilkan tabel data.

Memungkinkan pengguna memperbarui data tertentu dengan tetap mempertahankan nilai lama jika tidak diubah.

Lihat Semua Data `(Menu 4)`:

Menampilkan semua data yang tersimpan di data_table.

Keluar `(Menu 5)`:

Mengakhiri program.

# Code Data
```python
class Data_Pendaftaran:
    def __init__(self, name, nim, phone, email):
        self.name = name
        self.nim = nim
        self.phone = phone
        self.email = email
```

# Code Process
```python
import re
from Data.Data1 import Data_Pendaftaran
from View.View1 import view_pendaftaran


class process_pendaftaran:
    def validate_name(name):
        if not name.isalpha():
            raise ValueError("Nama hanya boleh berisi huruf.")
        
    def validate_nim(nim):
        if not nim.isdigit():
            raise ValueError("NIM hanya boleh berisi angka.")

    def validate_phone(phone):
        if not phone.isdigit():
            raise ValueError("Nomor telepon hanya boleh berisi angka.")

    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email harus valid, mengandung '@' dan '.'.")

    def validate_data(data):
        process_pendaftaran.validate_name(data.name)
        process_pendaftaran.validate_nim(data.nim)
        process_pendaftaran.validate_phone(data.phone)
        process_pendaftaran.validate_email(data.email)
```

# Code View
```python
from Data.Data1 import Data_Pendaftaran

class view_pendaftaran:
    def get_input():
        name = input("Nama: ")
        nim = input("NIM: ")
        phone = input("Nomor Telepon: ")
        email = input("Email: ")
        return name, nim, phone, email

    def table_view(data_table):
        print("=" * 95)
        print("| NO |           NAMA           |     NIM     |     NO TELEPON     |          EMAIL          |")
        print("=" * 95)

        for i, data in enumerate(data_table, start=1):
            print(f"| {i:<2} | {data.name:<30} | {data.nim:<13} | {data.phone:<19} | {data.email:<28} |")
        print("=" * 95)

    def display_message(message):
        print(message)
```

# Code Main
```python
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
```

# Hasil

<img width="446" alt="Screenshot 2025-01-10 150551" src="https://github.com/user-attachments/assets/78475347-2f64-4fae-8d9b-1a7e2339625c" />

<img width="452" alt="Screenshot 2025-01-10 150641" src="https://github.com/user-attachments/assets/600dc353-6aa6-45e1-a0df-1948c9f2337b" />

![Screenshot 2025-01-10 150722](https://github.com/user-attachments/assets/97022fb4-442e-4989-9df9-d27bcfbd5ca6)
