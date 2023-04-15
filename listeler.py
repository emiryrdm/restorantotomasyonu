class masa:

    def __init__(self, numara, konum):
        self.numara = numara
        self.konum = konum
        self.status = True

masa1 = masa("1","Bahçe")
masa2 = masa("2","Bahçe")
masa3 = masa("3","Bahçe")
masa4 = masa("4","Bahçe")
masa5 = masa("5","Bahçe")
masa6 = masa("6","Bahçe")
masa7 = masa("7","Salon")
masa8= masa("7","Salon")
masa9= masa("7","Salon")
masa10= masa("7","Salon")
masa11= masa("7","Salon")
masalar = [masa1,masa2,masa3,masa4,masa5,masa6,masa7,masa8,masa9,masa10,masa11]

class garson:

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

Ahmet = garson("Ahmet","Kibar","3650")
Kemal = garson("Kemal","Binbaşar", "4900")
Hasan = garson("İhsan","Yüce","3600")
Erhan = garson("Erhan","Ölmez","3460")

garsonlar = [Ahmet,Kemal,Hasan,Erhan]
