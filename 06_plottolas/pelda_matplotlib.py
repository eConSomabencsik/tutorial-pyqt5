import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

# Beimportáljuk a matplotlib PyQt5 kompatibilis megjelenítő felületét
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# Beimportáljuk a matplotlib PyQt5 kompatibilis megjelenítő toolbar-ját
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# Importáljuk a matplotlib alap plottolóját, az előző importok arra kellettek, hogy amit ezzel a plt-vel plottolunk az a GUI-n
# jelenjen meg és ne egy új ablakba, amit alapból létrehoz
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        layout = QVBoxLayout()

        self.figure = plt.figure() # Létrehozunk egy plottot, erre fog menni a plottolás
        self.canvas = FigureCanvas(self.figure) # Létrehozunk egy vászont aminek meg adjuk az előbb létrehozott plotot és ezt jelenítjük
                                                # meg a GUI-n
        toolbar = NavigationToolbar(self.canvas) # Létrehozunk egy toolbar, amivel majd könnyen kezelhetjük a felületet

        button = QPushButton("plot") # Gomb ahhoz, hogy plottoljunk görbét
        button.clicked.connect(self.plot)

        # Az imént létrehozott widget-eket rárakjuk a layoutra
        layout.addWidget(self.canvas)
        layout.addWidget(toolbar)
        layout.addWidget(button)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def plot(self): # Metódus egy görbe plottolásához
        self.figure.clear() # Elöszőr letisztítjuk a plotot (Ez törli az eddig megjelenített görbéket)

        # Meghatározzuk az x és y koordinátákat külön-külön
        x = [0, 1, 2, 3, 4, 5]
        y = [2, 3, 9, 4, 5, 1]

        ax = self.figure.add_subplot(111) # A plotra rakunk egy "rész-plotot"
        ax.plot(x, y) # Erre a rész-plotra plottoljuk a meghatározott x és y értékeket

        self.canvas.draw() # Frissítsük a vásznat, mivel alapjáraton nem frissül a plot
        # Fontos! Ha ezt nem tesszük meg, akkor nem fog látszani a plot!

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()