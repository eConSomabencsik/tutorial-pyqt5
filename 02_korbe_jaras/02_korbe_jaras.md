# Korbe jaras

A videót megtekintve rakjunk össze valami egyszerű GUI-t, lehet mint a végén egy egyszerű label + gomb és azt mentsük le, ez egy .ui kiterjesztésű fájlt fog eredményezni. <br>
Ahhoz, hogy ezt a .ui-t python kódra átfordítsuk a következő parancsot kell lefuttatni terminálba (Windowson command line-ban): ```pyuic5 -o <python file neve> <.ui file neve>``` <br>
Jelen szituációban: ```pyuic5 -o baseWindow.py example.ui``` <br>
Majd az "example.py" futattásával megtudjuk tekinteni ezt a minimalisztikus GUI-t.