import time
from listeler import masalar
import matplotlib.pyplot as plt
from listeler import garsonlar


class masa:

    def __init__(self, numara, konum):
        self.numara = numara
        self.konum = konum
        self.status = True

    def ekleMasa():
        x = masalar[-1].numara
        x = int(x)
        x = x + 1
        x = str(x)
        r1 = ("x" + "masa")
        y = str(input("Masayı Nereye Eklemek İstiyorsunuz: ")).capitalize()

        if y == "Bahçe":
            r1 = masa(x, y)
            masalar.append(r1)
            print("Masa Eklendi")
        if y == "Salon":
            r1 = masa(x, y)
            masalar.append(r1)
            print("Masa Eklendi")

    def silMasa():
        
                
        param = int(input("Hangi Masayı Silmek İstiyorsunuz: "))
        h1 = masalar[param - 1].numara
        masalar.pop(param - 1)
        print("masa" + h1 + " " + "Başarıyla Silindi")

    def masalarıListele():
        for i in masalar:
            print("masa" + i.numara + "" + f"{[i.konum]}")


class garson:

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def garsonlarıListele():
        for i in garsonlar:
            print(i.ad + " " + i.soyad)

    def garsonEkle():
        Garson_İsmi = input("Garson İsmi: ").capitalize()
        Garson_Soyad = input("Garson Soyismi: ").capitalize()
        Garson_Maas = input("Garson Maaşı ").capitalize()
        yeniGarson = garson(ad=Garson_İsmi, soyad=Garson_Soyad, maas=Garson_Maas)
        x = yeniGarson.ad + " " + yeniGarson.soyad + " " + yeniGarson.maas
        garsonlar.append(yeniGarson)
        print(yeniGarson.ad + " " + yeniGarson.soyad + " " + "Başarıyla Eklendi")

    def garsonSil():
        x = -1
        y = 0
        while True:
            x += 1
            y += 1
            print(garsonlar[x].ad + " " + garsonlar[x].soyad + " " + "Silmek İçin" + " " + f"{y}" + " " + "Tuşlayınız")
            if x == len(garsonlar) - 1:
                break
        param = int(input("Hangi Garsonu Silmek İstiyorsunuz: "))
        h1 = garsonlar[param - 1].ad
        garsonlar.pop(param - 1)
        print(h1 + " " + "Başarıyla Silindi")


def restorantGraph():
    plt.figure(figsize=(8,12))
    plt.title("Envanter", color="red")
    plt.xlabel("Garson Sayısı", color="green", size=12)
    plt.ylabel("Adet", color="orange", size=12)
    plt.bar("Garson Sayısı", len(garsonlar))
    plt.bar("Masa Sayısı", len(masalar))
    plt.show()


while True:
    try:
        print(""" 

        [1] MASALARI GÖRÜNTÜLEMEK İÇİN

        [2] GARSONLARI GÖRÜNTÜLEMEK İÇİN

        [3] MASA EKLEMEK İÇİN

        [4] GARSON EKLEMEK İÇİN

        [5] MASA SİLMEK İÇİN

        [6] GARSON SİLMEK İÇİN

        [7] GRAFİKLERE ERİŞMEK İÇİN

        [8] ÇIKIŞ YAPMAK İÇİN    

    """)
        t = int(input("Hangi İşlemi Yapmak İstiyorsunuz: "))

        if t == 1:
            masa.masalarıListele()
            time.sleep(2)

        if t == 2:
            garson.garsonlarıListele()
            time.sleep(2)

        if t == 3:
            masa.ekleMasa()
            time.sleep(2)

        if t == 4:
            garson.garsonEkle()
            time.sleep(2)

        if t == 5:
            masa.silMasa()
            time.sleep(2)

        if t == 6:
            garson.garsonSil()
            time.sleep(2)

        if t == 7:
            restorantGraph()

        if t == 8:
            print("Çıkış Yapılıyor....")
            time.sleep(3)
            quit()
    except ValueError or TypeError():
        continue

