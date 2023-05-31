import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget # Importáljuk a PlotWidget-et, amivel majd görbéket tudunk megjeleníteni
from pyqtgraph import mkPen # az mkPen egy metódus, ami egy QPen-t ad vissza, ezzel tudjuk beállítani,
                            # hogy hogyan szeretnénk görbéket megjeleníteni (szín, vastagság, típus, ...)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plotWidget = PlotWidget() # Létrehozzuk a plot widgetet

        x = [0, 1, 2, 3, 4, 5] # Megadjuk az x koordinátákat
        y = [2, 5, 1, 9, 2, 3] # Megadjuk az y koordinátákat
        # Ezek a koordináták, majd össze lesznek párosítva, tehát (0, 2), (1, 5), ...

        self.plotWidget.setBackground("w") # Beállítjuk a plot háttérszínét fehérre (w -> white), mivel alapból fekete

        pen = mkPen(color=(200, 0, 0), width=5) # Létrehozunk egy "toll"-at, amivel megadjuk, hogy a színét és vastagságát

        self.plotWidget.plot(x, y, pen=pen) # Kiplottoljuk az x és y koordinátákat az imént létrehozott "toll"-al
        
        self.setCentralWidget(self.plotWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()