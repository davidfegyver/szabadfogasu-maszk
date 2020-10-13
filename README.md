# <p align="center"> Egy Maszk érzékelős ajtó/jelző rendszer  </p>
## <p align="center"> Egy projekt a  C3 versenyére</p>
https://verseny.c3.hu

![c3](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/c3verseny.png)                                                
Itt a nyakunkon a második hullám.
A kormány rendeleteket hozott. Kötelező a maszkviselés a tömegközlekedési eszközökön, üzletekben, moziban, és sok helyen az iskolákban is.  

Ez a maszk érzékelős ajtó megakadályozza a koronavírussal nem törődő embereket hogy belépjenek például a könyvtárba, bevásárlóközpontokba és zárt helyekre.
Így nem kell a biztonsági őröknek ezekre az emberekre figyelni. 
Ez biztonságosabbá teszi az dolgozók munkáját, és az emberek életét.


## :star: Funkciók
* Maszk érzékelés
* Arduino alapú ajtó nyitás (relével)
* Arduino alapú ledek (Piros - Nincs maszk, Zöld - Van (Ekkor nyit ki az ajtó))
* Arduino alapú riasztó ami bekapcsol ha nincs rajtad maszk

Ez a projekt felhasználható rengeteg más projekthez is, sőt még [Raspberry Pire (3/4)](https://www.raspberrypi.org/) vagy [Nvidia Jetsonra](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/) is felteheted!

## :robot: Telepítés

Minden telepítendő könyvtár fel van sorolva a  [`requirements.txt`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/requirements.txt)ben.

0. Nyiss meg egy terminált/parancssort.

1. Töltsd le a repot.
```
$ git clone https://github.com/davidfegyver/szabadfogasu-maszk/
```

2. Lépj be a letöltött mappába: 
```
$ cd szabadfogasu-maszk/
```

3. Most írd be ezt hogy telepítsd a szükséges könyvtárakat. Ez lehet sok idő lesz a neted sebességétől függően.
```
$ pip3 install -r requirements.txt

```
#### Arduino beállítása (Nem kötelező)
Töltsd fel ezt a kódot: [`maszk.ino`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino)
Építs egy ilyesmi áramkört
![arduino schema](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/schema.png)


## :bulb: Futtatás

1. Nyisd meg a terminált, lépj be a letöltött mappába, és futtasd ezt a parancsot:
```
$ python3 maskdetector.py
```

Válaszolj a megadott kérdésekre(Van-e arduinod? Ha igen, mi a portja?), és várd meg amíg elindul a program. Ha minden sikeres akkor be fog jönni a kamerád képe, és láthatod hogy van-e rajtad maszk.

## Képek

TODO

## 🖥️ Felhasznált könyvtárak/projektek

- [OpenCV](https://opencv.org/)
- [Caffee alapú arc érzékelő](https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/resnet_ssd_face_python.py)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## TODO:
  * Hőmérés
  * További ötletek jöhetnek pull requestben :)

## 🎉 Köszi hogy végignézted
Ha bármi problémád akadt akkor kérlek írj nekem egy emailt: `fegyverdavid.bator@gmail.com` vagy nyiss egy Issuet itt: [Szabadfogasu-maszk](https://github.com/davidfegyver/szabadfogasu-maszk/issues)
![](https://komarev.com/ghpvc/?username=szabadfogasumaszkprojekt&color=lightgreen)

## :handshake: Hozzájárulás
Ha lenne valami ötleted, vagy kijavítanál egy bugot akkor nyiss egy **Pull requestet**. 

**Ha tetszett a projekt adhadsz is egy csillagot :D**

## 📝 Liszensz

**GNU GPLv3**
https://choosealicense.com/licenses/gpl-3.0/
