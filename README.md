[Switch to English :england:](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/README_English.md)
# <p align="center"> Egy Maszk érzékelős ajtó/jelző rendszer (Maszkimum) </p>
## <p align="center"> Egy projekt a  C3 Szabadfogású Számítógép versenyére<p>
<img src="https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/c3verseny.png" width="250"/>

### :star::star: Nyerteem!!
##### Köszönöm a C3 alapítványnak és a Számlázz.hu IT vezetőjének a kiválasztást! Az értékelőt/verseny bemutatóját erről a projektről [ITT](https://verseny.c3.hu/2020/#nyertesek/FD) tudjátok megnézni.

Itt a nyakunkon a második hullám.
A kormány rendeleteket hozott. Kötelező a maszkviselés a tömegközlekedési eszközökön, üzletekben, moziban, és sok helyen az iskolákban is.  

Ez a maszk érzékelős ajtó megakadályozza a koronavírussal nem törődő embereket attól, hogy belépjenek például a könyvtárba, bevásárlóközpontokba és zárt helyekre, így nem kell a biztonsági őröknek ezekre az emberekre figyelni.
Ez biztonságosabbá teszi az dolgozók munkáját, és az emberek életét.


## :star: Funkciók
* Maszk érzékelés
* Arduino-alapú ajtónyitás (relével)
* Arduino-alapú ledek (Piros - Nincs maszk, Zöld - Van (Ekkor nyit ki az ajtó))
* Arduino-alapú riasztó, ami bekapcsol ha nincs rajtad maszk

Ez a projekt felhasználható rengeteg más projektben is, sőt még [Raspberry Pire (3/4)](https://www.raspberrypi.org/) vagy [Nvidia Jetsonra](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/) is felteheted!

## :robot: Telepítés

Minden telepítendő könyvtár fel van sorolva a  [`requirements.txt`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/requirements.txt)ben.

0. Nyiss meg egy terminált/parancssort.

1. Töltsd le a repot:
```
$ git clone https://github.com/davidfegyver/szabadfogasu-maszk/
```

2. Lépj be a letöltött mappába:
```
$ cd szabadfogasu-maszk/
```

3. Most írd be ezt a parancsot, hogy telepítsd a szükséges könyvtárakat. Ez sok idő lehet a neted sebességétől függően.
```
$ pip3 install -r requirements.txt

```
#### Arduino beállítása (Nem kötelező)
Töltsd fel ezt a kódot: [`maszk.ino`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino) (`wget https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino`, vagy `curl -o ./maszk.ino https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino`)

Építs egy ilyesmi áramkört:
![arduino schema](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/schema.png)

#### Webes API használata
A webes API-ból adatokat lekérni JSON formázással lehet az `5000`-es porton. A webes API kétféle formátumot támogat: a `prettyStatus`, és a `shortStatus` formátumot

Példák a JQ JSON feldolgozóval GNU/Linux alatt:

```bash
$ curl -s http://localhost:5000 | jq .prettyStatus
```

Kimenet:

`Not wearing mask`

```bash
$ curl -s http://localhost:5000 | jq .shortStatus
```

Kimenet:

`False`

## :bulb: Futtatás

1. Nyisd meg a terminált, lépj be a letöltött mappába, és futtasd ezt a parancsot:
```
$ python3 maskdetector.py
```
Ha van arduinod, add hozzá ezt: -a COM4 (comport száma)
```
$ python3 maskdetector.py -a COM4
```

Várd meg, amíg elindul a program. Ha minden sikeres akkor be fog jönni a kamerád képe, és láthatod hogy van-e rajtad maszk.

## Bemutató videó
https://www.youtube.com/watch?v=eLyNWEL1Los

## 🖥️ Felhasznált könyvtárak/projektek

- [OpenCV](https://opencv.org/)
- [Caffee alapú arc érzékelő](https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/resnet_ssd_face_python.py)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## TODO:
  * Hőmérés
  * További ötletek jöhetnek pull requestben :)

## 🎉 Köszi, hogy végigolvastad
Ha bármi problémád akadt, akkor kérlek írj nekem egy emailt: `fegyverdavid.bator@gmail.com`, vagy nyiss egy Issuet itt: [Szabadfogasu-maszk](https://github.com/davidfegyver/szabadfogasu-maszk/issues)


## :handshake: Hozzájárulás
Ha lenne valami ötleted, vagy kijavítanál egy bugot, akkor nyiss egy **Pull requestet**.

Hozzájárulók:
- [Fegyver Dávid](https://github.com/davidfegyver)
- [PiciAkk](https://github.com/piciakk)

**Ha tetszett a projekt, adhadsz is egy csillagot :D**

## 📝 Licence

**MIT**
https://choosealicense.com/licenses/mit/
