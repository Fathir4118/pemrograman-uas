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
