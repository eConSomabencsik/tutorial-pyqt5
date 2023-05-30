import sys # Szükséges, mert ha esetleg argumentumokat szeretnénk megadni a GUI-nak, akkor azt itt lehet átadni

from PyQt5.QtWidgets import QMainWindow # Ezzel az importtal mondjuk meg, hogy egy Ablakot szeretnénk majd megnyitni
from PyQt5.QtWidgets import QApplication # Mielőtt létrehozzunk egy ablakot, amit megnyitunk a PyQt-ból egy applikációt kell létrehozni
                                         # ami majd tudja, hogy a következő ablakot hogyan jelenítse meg

from baseWindow import Ui_MainWindow # A generált ablaknak a kinézetét importáljuk ezzel a kóddal

class MainWindow(QMainWindow, Ui_MainWindow): # Létrehozunk egy új class-t, ami magába fogalalja egy MainWindow-nak a tulajdonságait
                                              # és a generált UI-nak az összerakó metódusát
    def __init__(self): # Egyszerű python konstruktor
        super().__init__() # Meghívjuk a szülő classoknak a konstruktoraikat (Mivel a Ui_MainWindow-nak nincsen, így csak a QMainWindow-ét)
        self.setupUi(self) # Ezzel a kóddal állítjuk össze a GUI-t

if __name__ == "__main__": # Ezzel a sorral biztosítjuk azt, hogy csak akkor fusson le ez a kód, amikor lefuttatjuk, enélkül
                           # a fájl importálása esetén is lefutna a következő pár sor
    app = QApplication(sys.argv) # Létrehozzuk a PyQt5 applikációt, ami majd később megjeleníti az ablakot és kezel alap funkciókat
                                 # Ilyen funkciók például az ablak bezárás, letálcázás, ...
    window = MainWindow() # A fent definiált osztályt létrehozzuk
    window.show() # Megmutatjuk a létrehozott ablakot, alapjáraton csak létrehoznánk és a háttérben futna, anélkül, hogy tudnánk róla
    app.exec() # Futtatjuk az adott alkalmazást
