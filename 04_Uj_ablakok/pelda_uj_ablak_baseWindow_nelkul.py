import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        valami: QWidget = Valami() # Hozzuk létre a lent definiált widgetet
        self.setCentralWidget(valami) # Most ahelyett, hogy megmutatnánk, beállítjuk a fő ablakunkra

class Valami(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        layout2 = QHBoxLayout()
        label = QLabel("A gomb nincs lenyomva")
        button = QPushButton("Klikkelj!")

        layout2.addWidget(label)
        layout2.addWidget(button)

        slider = QSlider(Qt.Orientation.Horizontal)

        layout.addLayout(layout2)
        layout.addWidget(slider)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
