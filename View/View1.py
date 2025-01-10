from Data.Data1 import Data_Pendaftaran

class view_pendaftaran:
    def get_input():
        print("Masukan Data Diri Anda")
        name = input("Nama: ")
        nim = input("NIM: ")
        phone = input("Nomor Telepon: ")
        email = input("Email: ")
        return name, nim, phone, email

    def table_view(data_table):
        print("=" * 99)
        print("| NO |           NAMA           |     NIM     |     NO TELEPON     |             EMAIL            |")
        print("=" * 99)

        for i, data in enumerate(data_table, start=1):
            print(f"| {i:<2} | {data.name:<24} | {data.nim:<11} | {data.phone:<18} | {data.email:<28} |")
        print("=" * 99)

    def display_message(message):
        print(message)
