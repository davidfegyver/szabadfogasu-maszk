<h1 align="center"> Egy Maszk érzékelős ajtó/jelző rendszer  </h1>
<h2 align="center"> Egy projekt a [C3 versenyére](https://verseny.c3.hu) </h2>

Itt a nyakunkon a második hullám.
A kormány rendeleteket hozott. Kötelező a maszkviselés a tömegközlekedési eszközökön, üzletekben, moziban, és sok helyen az iskolákban is.  

Ez a maszk érzékelős ajtó megakadályozza a koronavírussal nem törődő embereket hogy belépjenek például a könyvtárba, bevásárlóközpontokba és zárt helyekre.
Így nem kell a biztonsági őröknek ezekre az emberekre figyelni. 
Ez biztonságosabbá teszi az dolgozók munkáját, és az emberek életét.

## 🖥️ Felhasznált könyvtárak/projektek

- [OpenCV](https://opencv.org/)
- [Caffee alapú arc érzékelő](https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/resnet_ssd_face_python.py)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## :star: Funkciók
* Maszk érzékelés
* Arduino alapú ajtó nyitás (relével)
* Arduino alapú ledek (Piros - Nincs maszk, Zöld - Van (Ekkor nyit ki az ajtó))
* Arduino alapú riasztó ami bekapcsol ha nincs rajtad maszk

Ez a projekt felhasználható rengeteg más projekthez is, sőt még [Raspberry Pire (3/4)](https://www.raspberrypi.org/) vagy [Nvidia Jetsonra](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/) is felteheted!
