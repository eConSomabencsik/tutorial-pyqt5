import sys
import time
import logging

from PyQt5.QtWidgets import\
    QMainWindow, QApplication, QWidget, QVBoxLayout, \
    QPushButton, QPlainTextEdit
from PyQt5.QtCore import QObject, pyqtSignal, QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        valami = Valami()
        self.setCentralWidget(valami)

class Valami(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        logger = QTextEditLogger(self) # saját widget, amire majd loggoljuk az eredményeket
        logging.getLogger().addHandler(logger) # a beépített logging könyvtárnak a kezelőjéhez, hozzáadjuk a widgetünket
        logging.getLogger().setLevel(logging.INFO) # Beállítjuk a logging-nak, hogy milyen log szövegeket szeretnénk megjeleníteni
        # Ez azt jelenti, hogy ezt állíthatjuk DEBUG-ra, ERROR-ra is és akár külön "QTextEditLogger"-en is megjeleníthetjük őket

        button = QPushButton("Klikkelj!")
        button.clicked.connect(self.runFibo)

        layout.addWidget(button)
        layout.addWidget(logger.widget)
        
        self.setLayout(layout)

    def runFibo(self):
        self.fiboRunner = FiboRunner(2) # Létre hozzuk a Fibonacci futattó objektumunkat, ami majd egy másik szálon fog futni,
                                        # hogy a GUI-t ne fagyassza le
        self.fiboRunner.start() # Elindítjuk a létrehozott "szálat"

class FiboRunner(QThread): # Class amit a QThread osztályból származtatunk, hogy meglegyenek az egy szálhoz való összes tulajdonsága
    def __init__(self, n: int): # Konstruktor aminek jelenleg itt adjuk át, hogy a fibonacci sor hányadik számát szeretnénk megkapni
        super().__init__()
        self.n = n

    def run(self): # Ezt a függvényt fogja a szál lefutattni
        logging.info(f"Result: {fibo(self.n)}") # Kiloggoljuk a kapott eredményt

class QTextEditLogger(logging.Handler, QObject): # Class ahhoz, hogy könnyen tudjunk loggolni GUI-ra
    appendPlainText = pyqtSignal(str) # Egy pyqtSignal, ugyanolyan, mint a QPushButton-nak a "clicked", csak ezt mi írjuk meg

    def __init__(self, parent):
        super().__init__()
        QObject.__init__(self)
        self.widget = QPlainTextEdit(parent) # Ez lesz a fő widget, amit a végén kirakunk a GUI-ra
        self.widget.setReadOnly(True) # Ezzel beállítjuk azt, hogy a felhasználó módosíthatja a szöveget 
        self.appendPlainText.connect(self.widget.appendPlainText) # Az általunk létrehozott Signal-ra rákötjük a widget egyik metódusát,
        # aminek alapjáraton vár egy argumentumot, de a Signal-t úgy is hoztuk létre, hogy megadtuk neki, hogy egy stringet fog átadni

    def emit(self, record): # Ezzel a metódussal fogjuk majd a szöveget a widget-re tenni
        msg = self.format(record) # Megformázzuk a szöveget a "logging"-nak beállított formázás alapján, ez jelenleg az alap
        self.appendPlainText.emit(msg) # Leadunk egy signal-t az általunk megírt signal-ön keresztül és átadjuk neki az információt
        # És mivel összekötöttük azt a widget-tel, ezért azonnal meg is jelenik a log üzenet

# Kalsszikus fibonacci sor metódus
def fibo(n):
    logging.info(f"{n}") # Loggoljuk a jelenleg számolt értéket, csak azért kell, hogy valami megjelenjen a GUI-n a végeredményen kívül
    time.sleep(1) # Várunk 1 másodpercet, hogy bemutassam tényleg szépen egyesével loggol a program
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
