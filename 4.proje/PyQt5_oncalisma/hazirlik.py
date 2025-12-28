# PyQt5 nedir ? --> Python ile masaüstü GUI uygulamaları yapmamızı sağlar.
    # GUI --> Graphical User Interface
# PyQt5 ile normal Python'u görsel hale getiririz.

# sys kütüphanesini import etmemiz istenir. Bu zorunludur.
    # sys kütüphanesi GUI uygulamalarının çalışması için zorunludur.
    # sys.argv ile argv ( argument and value ) en başta alınır.
    # Bu komut ile programın nasıl çalıştırıldığı ve sistemden gelen ayarlar belirlenir.


# PyQT5 bizim GUI yapmamızı sağlayan ana kütüphanedir.
    # PyQT5 içinde Pencere , buton , yazı , menü gibi yüzlerce hazır parça mevcuttur.
    # QTWidgets : PyQT5'in görsel bileşenlerini içeren bölümdür. Yani ekranda gördüğümüz her şeydir.
    # QApplication : Uygulamanın ana merkezidir. Fare , klavte ve pencere olayları yönetilir.
    # QWidget : En temel penceredir. Buton , yazı ve buna benzer her şey bunun içine konur.
    # QPushButton : Tıklanabilen buton oluşturmak için kullanılır. QPushButton("Tıkla", window) şeklinde ismine isim de yazılabilir.

# Özellikler : 

    # Label( etiket ) ekleme :
        # Ekranda sabit bir yazı göstermek için kullanılır.
        # QTWidgets kütüphanesinden QLabel ile etiket alırız.
        # setText ile metin yazabiliriz.

    # Kullanıcının girmesi için alan :
        # QTWidgets kütüphanesinden QLineEdit ile alırız.



# Buton = Kullanıcının tıklayarak komut verdiği nesnedir.
    # PyQT5'te adı QPushButton'dur.
import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

def kaydedildi():
    print("Kaydedildi!")

def bilgi_yazdir():
    ad_bilgisi = ad_kutusu.text()
    soyad_bilgisi = soyad_kutusu.text()
    ÖğrenciNo_bilgisi = int(numara_kutusu.text())
    print("Kişi bilgileri:")
    print("Ad :",ad_bilgisi , " Soyad:",soyad_bilgisi , "Öğrenci Numarasi:",ÖğrenciNo_bilgisi)

def dosyaya_kaydet():
    ad_kutusu1 = ad_kutusu.text()
    soyad_kutusu1 = soyad_kutusu.text()
    numara_kutusu1 = numara_kutusu.text()

    if not (numara_kutusu1.isdigit()):
        numara_kutusu.setPlaceholderText("Sadece sayı giriniz")
        return

    Ogrenci = {
        "ad":ad_kutusu1,
        "soyad": soyad_kutusu1,
        "numara": int(numara_kutusu1)
    }

    with open("ogrenci_bilgileri.json","a",encoding="utf-8") as file1:
        json.dump(Ogrenci,file1)
        file1.write("\n")

    print("Json dosyasina kaydetme işlemi başarili!")


window = QWidget()
window.setWindowTitle("Öğrenci Bilgi sistemi")
window.resize(400,300)

Label_ad = QLabel("Ad :",window)
Label_ad.move(50,50)

label_soyad = QLabel("Soyad :",window)
label_soyad.move(50,100)

label_ogrenciNo = QLabel("Öğrenci No :",window)
label_ogrenciNo.move(50,150)

ad_kutusu = QLineEdit(window)
ad_kutusu.move(100,50)

soyad_kutusu = QLineEdit(window)
soyad_kutusu.move(100,100)

numara_kutusu = QLineEdit(window)
numara_kutusu.move(130,150)

resim_label = QLabel(window)
resim_label.setPixmap(QPixmap("logo.png"))
resim_label.move(200,20)
resim_label.resize(150, 150)


button = QPushButton("Kaydet",window)
button.move(100,250) # ilk sayı : sağa / ikici sayi : aşağı
button.clicked.connect(kaydedildi)
button.clicked.connect(bilgi_yazdir)
button.clicked.connect(dosyaya_kaydet)


window.show()



sys.exit(app.exec_())
