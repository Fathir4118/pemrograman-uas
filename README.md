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


# Code Process


# Code View


# Code Main


# Hasil
