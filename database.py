import function
import sqlite3

kaynak = sqlite3.connect("dersler.db")

islem0 = "CREATE TABLE IF NOT EXISTS dersler(Ders_Adi text, Ders_Sayisi int, Ders_Saati datetime)"
function.ders_listele()
kaynak.commit()

islem = "INSERT INTO dersler where Ders_Adi"
function.ders_ekle()
kaynak.commit()

islem2="DELETE from dersler where Ders_Adi"
function.ders_silme()
kaynak.commit()

islem3="UPDATE dersler WHERE Ders_Adi= ?"
function.ders_guncelle("Sosyal Bilimler")
kaynak.commit()

kaynak.close()
