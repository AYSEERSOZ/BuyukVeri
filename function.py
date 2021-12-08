def ders_listele(kaybak, listele):
    komut0=kaynak.cursor()
    islem0=listele
    komut0.execute(islem0)
    return komut0
    
def ders_ekle(kaynak, ekle):
    komut=kaynak.cursor()
    islem=ekle
    komut.execute(islem)
    return komut

def ders_silme(kaynak, silme):
    komut2=kaynak.cursor()
    islem2=silme
    komut2.execute(islem2)
    return komut2


def ders_guncelle(kaynak, guncelle):
    komut3=kaynak.cursor()
    islem3=guncelle
    komut3.execute(islem3)
    return komut3
