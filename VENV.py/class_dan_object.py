class Perusahaan:
    def __init__(self, nama, lokasi):
        self.nama = nama
        self.lokasi = lokasi

    def info(self):
        return f"Perusahaan {self.nama} berlokasi di {self.lokasi}."
class Karyawan:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi

    def info(self):
        return f"Karyawan {self.nama} bekerja sebagai {self.posisi}."
    
perusahaan = Perusahaan("Tech Innovators", "Jakarta")
karyawan = Karyawan("Andi", "Software Engineer")
print(perusahaan.info())
print(karyawan.info())
