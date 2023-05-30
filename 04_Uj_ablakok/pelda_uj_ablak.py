import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QWidget # A "QWidget"-tel tudunk új ablakokat benyitni, ha már van egy MainWindow-unk
from PyQt5.QtWidgets import QVBoxLayout # Ez a layout azt teszi eléhetővé, hogy amilyen widgetek belepakolunk, azok egymás alatt szépen
                                        # ugyanakkora helyen elférnek, továbbá ha változtatunk az ablak méretén, akkor reszponzívan
                                        # újraméretezi a benne lévő widgeteket
from PyQt5.QtWidgets import QHBoxLayout # Ugyanaz, mint az előző, csak ez horizontálisan csinálja meg azt, amit a másik vertikálisan
from PyQt5.QtWidgets import QLabel, QPushButton, QSlider # A már megismert widgeteket beimportájuk, amiket az új ablakra szeretnénk rakni
from PyQt5.QtCore import Qt # Ez csak arra kell, hogy a slider ne függőlegesen jelenjen meg, hanem horizontálisan

from baseWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.setText("Klikkelj!")
        self.pushButton.clicked.connect(self.GombKlikk)

    def GombKlikk(self):
        # Start
        self.valami = Valami() # Létrehozzuk az új ablakot
        self.valami.show() # Ugyanúgy, mint a főablakot, ezt sem jelenitjük meg alapjáraton, így nekünk kell kézzel megmutatni
        # End es a lokalis valtozokat dobjuk

class Valami(QWidget): # Az új ablak class-ja
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() # Ebbe a vertikális layout-ba fogjuk pakolni a további widgeteket
        
        layout2 = QHBoxLayout()
        label = QLabel("A gomb nincs lenyomva") # label
        button = QPushButton("Klikkelj!") # nyomógomb

        # A horizontális layoutba bepakoljuk a labelt és a gombot, vagyis egymás mellé rakjuk
        layout2.addWidget(label)
        layout2.addWidget(button)

        slider = QSlider(Qt.Orientation.Horizontal) # slider

        # Hozzá adjuk a layoutunkhoz fentebb létrehozott widgeteket/layoutokat, a sorrend, fontos!
        # Az első lesz legfelül, az utolsó lesz legalul
        layout.addLayout(layout2)
        layout.addWidget(slider)

        # Az új ablaknak megmondjuk, hogy ezt a layoutot szeretnénk beállítani, így ez fog megjelenni
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
