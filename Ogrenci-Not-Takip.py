class Ogrenci:
    def __init__(self, ad, soyad, numara, bolum):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.bolum = bolum
        self.dersler = []

    def ders_tanimla(self, ders_adi, vize = 0, final = 0):
        ders = {}
        ders["adi"] = ders_adi
        ders["vize"] = vize
        ders["final"] = final
        return ders
    
    def ders_ekle(self, ders_adi, vize = 0, final = 0):
        self.dersler.append(self.ders_tanimla(ders_adi, vize, final))

    def ders_sil(self, ders_adi):
        for ders in self.dersler:
            if ders["adi"] == ders_adi:
                self.dersler.remove(ders)

    def not_gir(self, ders_adi, sinav, notu):
        for ders in self.dersler:
            if ders["adi"] == ders_adi:
                if sinav == "vize":
                    ders["vize"] = notu
                else:
                    ders["final"] = notu

    def ortalama_hesaplama(self):
        for ders in self.dersler:
            ders["ortalama"] = ders["vize"] * 0.4 + ders["final"] * 0.6

    def ders_sonuc(self):
        for ders in self.dersler:
            if ders["ortalama"] >= 50:
                ders["sonuc"] = "GEÇTİ"
            else:
                ders["sonuc"] = "KALDI"


def ogrenci_ekle():
    ad = input("Öğrenci adını girin: ")
    soyad = input("Öğrenci soyadını girin: ")
    numara = input("Öğrenci numarasını girin: ")
    bolum = input("Öğrenci bölümünü girin: ")

    ogrenci = Ogrenci(ad, soyad, numara, bolum)

    devam = True
    while devam:
        ders_adi = input("Dersin adını girin: ")
        vize = int(input("Vize notunu girin: "))
        final = int(input("Final notunu girin: "))
        ogrenci.ders_ekle(ders_adi)
        ogrenci.not_gir(ders_adi, "vize", vize)
        ogrenci.not_gir(ders_adi, "final", final)
        
        giris = input("Ders eklemek istiyor musunuz? (E/H): ")
        if giris.upper() == "E":
            devam = True
        else:
            devam = False
        
    
    return ogrenci



def yazdır(Ogrenciler):
    for ogrenci in Ogrenciler:
        print(ogrenci.ad, ogrenci.soyad, ogrenci.numara)
        for ders in ogrenci.dersler:
            print(ders["adi"], "\nVize:", ders["vize"], "Final:", ders["final"], "Ortalama:", ders["ortalama"], "Sonuç:", ders["sonuc"])

        print("--------------------------------------------------")


Ogrenciler = []
devam2 = True
while devam2:
    ogrenci = ogrenci_ekle()
    ogrenci.ortalama_hesaplama()
    ogrenci.ders_sonuc()
    Ogrenciler.append(ogrenci)
    deger = input("Öğrenci eklemek istiyor musunuz? (E/H): ")
    if deger.upper() == "E":
        devam2 = True
    else:
        devam2 = False


yazdır(Ogrenciler)

