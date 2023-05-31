# Logging, threading

Ebben a részben azt mutatom be, hogyan tudunk egyszerűen loggolni GUI-ra. Egyszerű alatt azt értem, hogy nem egy widget-nek a valamelyik metódusát hívjuk meg és ott átadjuk a loggolni kívánt szöveget, hanem a beépített modult használjuk ehhez, tehát a ```logging``` könyvtárat <br><br>
Hogyha egy hosszabb futatást szeretnénk futattni és esetleg azt loggolni is szeretnénk valahogyan, akkor arra is mutatok megoldást. <br>
Hogy miért nem egyértelmű? <br>
* Mivel a futást elindítjuk, akkor a programra abba a kód részletbe ugrik be, ahol ugyan loggolja a jelenlegi eredményt, de nem tudja közben kezelni a GUI-nak a megjelenítését, tehát lefagy a program és a háttérben számol valamit
* Valahogy rákell kötni a logging függvényt az adott widget-re, hogy könnyen tudjuk kezelni