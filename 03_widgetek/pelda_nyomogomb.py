import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from baseWindow_gomb import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.labelhaha.setText("A gomb nincs lenyomva") # Beállítjuk a label szövegét
        self.pushButton.setText("Klikkelj!") # Beállítjuk a gomb szövegét
        self.pushButton.clicked.connect(self.GombKlikk) # Összekötjük a gomb lenyomása "Signal"-t, a "GombKlikk" metodussal

    def GombKlikk(self): # Metodus a gomb lenyomásához
        self.labelhaha.setText("a gomb le lett nyomva") # Átírjuk a label szövegét, a gomb lenyomása után

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
