# Új_ablakok

## Új ablak
Új ablak készítéséhez tulajdonképpen semmi más nem kell, csak hogy létrehozunk egy class-t, amit a QWdiget-ből származtatunk, majd azon belül létrehozunk néhány widgetet és a végén pedig egy layout-ra bedobjuk az összes widgetet/layoutot és a fő layoutot pedig beállítjuk a QWidget-nek, ```lasd: pelda_uj_ablak.py```

## Ablak létrehozása qtdesigner nélkül
Az előző példában az mutattam be, hogyan tudunk egy új ablakot megnyitni, azt az ablakot nem muszáj megnyitnunk, ha nem szeretnék QtDesigner-t nyitni, akkor egyszerűen beállíthatjuk azt az elkészített widget-et a fő ablakunknak <br>
```lasd: pelda_uj_ablak_baseWindow_nelkul.py```