import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from baseWindow_slider import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.labelhaha.setText("A gomb nincs lenyomva")
        self.pushButton.setText("Klikkelj!")
        self.pushButton.clicked.connect(self.GombKlikk)
        self.slider.valueChanged.connect(self.setSliderValue) # Összekapcsoljuk a slidernek a valueChanged signal-jét a setSliderValue metodushoz

    def GombKlikk(self):
        self.labelhaha.setText("a gomb le lett nyomva")

    def setSliderValue(self): # Metódus a label szövegének frissitésére
        self.labelhaha.setText(str(self.slider.value())) # Beállítjuk a label szövegének a slider jelenlegi értékét

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
