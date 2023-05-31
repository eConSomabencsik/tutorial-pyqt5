# Plottolás

Ebben a részben két féle módot is bemutatok arra, hogy hogyan tudunk plottolni PyQt5-ben <br>

## pyqtgraph
* A pyqtgraph nem jön a PyQt5 könyvtárral együtt, tehát ezt külön kell hozzáadni a python könyvtárakhoz, ezt könnyen a pip parancs segítségével tudjuk orvosolni, nyissunk egy terminált (Windows-on command line) és írjuk be ezt: ```pip install pyqtgraph```
* A pyqtgraph egy gyors echte pythonban írt könyvtár, ami szerintem a legalkalmasabb 2D és 3D plottoláshoz PyQt5 GUI-t használva

## Matplotlib
* Ez a könyvtár teljesen független a PyQt-tól, de ezt is természetesen lehet használni plottoláshoz
* A telepítéshez egyszerűen a terminálba (command line-ba) írjuk be a következőt: ```pip install matplotlib```
* A leggyakrabban használt könyvtár plottoláshoz (PyQt-on kívül)