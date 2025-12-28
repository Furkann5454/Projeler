# --------------- PyQt5 Arayüzü ------------
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from API_client import ucus_verisini_getir


class GrafikEkrani(FigureCanvas):
    def __init__(self, parent=None, genislik=5, yukseklik=4, dpi=100):
        self.sekil = Figure(figsize=(genislik, yukseklik), dpi=dpi)
        self.eksen = self.sekil.add_subplot(111, projection='3d')
        super(GrafikEkrani, self).__init__(self.sekil)

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proje Ödevi - 3D Uçuş Rotasi")
        self.setGeometry(100, 100, 1200, 800)

        self.merkez_widget = QWidget()
        self.setCentralWidget(self.merkez_widget)
        self.ana_layout = QHBoxLayout(self.merkez_widget)

        self.sol_kisim = QVBoxLayout()
        
        self.sol_kisim.addWidget(QLabel("Uçuş Numarasi (ID):"))
        self.txt_ucus_id = QLineEdit()
        self.sol_kisim.addWidget(self.txt_ucus_id)
        
        self.btn_sorgula = QPushButton("Rotayi Göster")
        self.btn_sorgula.clicked.connect(self.verileri_getir)
        self.sol_kisim.addWidget(self.btn_sorgula)

        self.txt_sonuc = QTextEdit()
        self.txt_sonuc.setReadOnly(True)
        self.sol_kisim.addWidget(self.txt_sonuc)
        
        self.ana_layout.addLayout(self.sol_kisim, 1)

        self.tuval = GrafikEkrani(self)
        self.ana_layout.addWidget(self.tuval, 3)

    def verileri_getir(self):
        girilen_id = self.txt_ucus_id.text()

        if not girilen_id:
            QMessageBox.warning(self, "Uyari", "Lütfen bir ID numarasi giriniz.")
            return

        gelen_veri, hata_mesaji = ucus_verisini_getir(girilen_id)

        if hata_mesaji:
            QMessageBox.warning(self, "Hata", hata_mesaji)
            self.txt_sonuc.clear()
        else:
            self.cizim_yap(gelen_veri)
            self.bilgileri_listele(gelen_veri)

    def cizim_yap(self, veri):
        self.tuval.eksen.cla()
        
        x_ekseni = [float(n['enlem']) for n in veri['noktalar']]
        y_ekseni = [float(n['boylam']) for n in veri['noktalar']]
        z_ekseni = [float(n['irtifa']) for n in veri['noktalar']]

        self.tuval.eksen.plot(x_ekseni, y_ekseni, z_ekseni, color='blue', linewidth=2, label=f"Uçuş {veri['id']}")
        
        self.tuval.eksen.scatter(x_ekseni[0], y_ekseni[0], z_ekseni[0], color='green', s=50, label='Kalkış')
        self.tuval.eksen.scatter(x_ekseni[-1], y_ekseni[-1], z_ekseni[-1], color='red', s=50, label='Varış')

        self.tuval.eksen.set_xlabel('Enlem')
        self.tuval.eksen.set_ylabel('Boylam')
        self.tuval.eksen.set_zlabel('İrtifa')
        self.tuval.eksen.legend()
        
        self.tuval.draw()

    def bilgileri_listele(self, veri):
        liste = veri['noktalar']
        baslangic = liste[0]
        bitis = liste[-1]
        
        metin = (f"Uçuş No: {veri['id']}\n"
                 f"Toplam Veri Sayısı: {len(liste)}\n\n"
                 f"BAŞLANGIÇ KONUMU:\nEnlem: {baslangic['enlem']}\nBoylam: {baslangic['boylam']}\nYükseklik: {baslangic['irtifa']}\n\n"
                 f"VARIŞ KONUMU:\nEnlem: {bitis['enlem']}\nBoylam: {bitis['boylam']}\nYükseklik: {bitis['irtifa']}")
        self.txt_sonuc.setText(metin)

if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(uygulama.exec_())