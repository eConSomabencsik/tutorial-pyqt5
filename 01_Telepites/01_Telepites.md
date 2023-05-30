# Python3, PyQt5 telepítés

## Python3

### Windows
- Windowson való használathoz javaslom a python 3.8.10es verziót (https://www.python.org/downloads/release/python-3810/)
    - 3.8as verzió alatt volt fejlesztve a PyQt5 nagyrészt és azért 3.8.10, mert az a legstabilabb változat
    - Ügyeljünk arra, hogy amikor telepítjük a pythont, akkor mindenképpen pipáljuk be, hogy a pip-et adja hozzá a windows környezeti változóihoz, ha nem tesszük meg, akkor kézzel kell ezt elvégezni

### Linux (Ubuntu)
- Linuxra alapból telepítve van egy python 3.x-es verzió, ennek a lecserlését nem javaslom
- Ami elképzelhető, hogy nincs alapjáraton telepítve az a pip
    - Ehhez egyszerűen terminálba beírjuk, hogy: ```sudo apt install python3-pip```

## QtDesginer

### Windows
- Windowsra szerencsére egyszerűen tudjuk telepíteni a segéd programot, hiszen csak letöltjük a telepítő fájlját és máris használhatjuk, ehhez a link: https://build-system.fman.io/qt-designer-download

### Linux (Ubuntu)
- Linuxra nincsen egy telepítő fájl, amit megnyitva csak feltelepül az alkalmazás
- Nyissunk egy terminált és írjuk be: ```sudo apt install qttools5-dev```

## PyQt5
- Végül pedig a legegyszerűbb, ez mind a két platformon ugyanúgy megy
    - Nyissunk meg egy terminált (Windows esetén command line-t) és írjuk be a következőt: ```pip install PyQt5```

## Utolsó lépések
Hogy meggyőződjünk arról, hogy sikerült a QtDesignert letölteni, nyissuk meg és amikor megnyílik válasszuk ki a "Main Window" opciót, majd kattintsunk a "create" gombra
Arról, hogy a python-t sikerült feltelepíteni az igazolja, hogy pip-pel PyQt5 telepítésénél nem jött elő semmi hiba