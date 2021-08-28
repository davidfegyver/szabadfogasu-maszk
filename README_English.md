[Switch back to Hungarian :hungary:](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/README.md)
# <p align="center"> Door opening/alarming system with mask-detection (Maszkimum) </p>
## <p align="center"> A project for the Szabadfogású Számítógép competition of C3<p>
<img src="https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/c3verseny.png" width="250"/>

### :star::star: I won the competition!!
##### Thanks to the C3 foundation and the IT leader of Számlázz.hu for choosing me! You can find the competition's description of my project [here](https://verseny.c3.hu/2020/#nyertesek/FD).

The second wave of COVID is coming...
The government made regulations...
It is mandatory to wear a mask on public transport, in stores, in the cinema, and in a lot of cases, in school.

This mask-detection door blocks people, who don't care about Coronavirus from entering the library, the shopping mall, and other closed places.
So security guards don't have to deal with these people.
This makes our life safer.


## :star: Functions
* Automatic mask detection
* Arduino-based door opening (with relay)
* Arduino-based leds (Red - no mask; Green - wearing mask (in case, the door is opening))
* Arduino-based alarm, which turns on if you don't have a mask on

This projects can also be used in many other project, you can even upload it to [Raspberry Pi](https://www.raspberrypi.org/) or to [Nvidia Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/)

## :robot: Installation

All the libraries/modules to install is listed in the [`requirements.txt`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/requirements.txt) file.

0. Open up a terminal/commandline.

1. Download/clone this repo.
```
$ git clone https://github.com/davidfegyver/szabadfogasu-maszk/
```

2. Go to the newly downloaded folder:
```
$ cd szabadfogasu-maszk/
```

3. Install the required modules. The download speed may vary, depending on your internet connection.
```
$ pip3 install -r requirements.txt

```
#### Setting up Arduino (Optional)
Download the source code for your Arduino: [`maszk.ino`](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino) (`$ wget https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino` or `curl -o ./maszk.ino https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/maszk.ino`)

And build a circuit like that:
![arduino schema](https://github.com/davidfegyver/szabadfogasu-maszk/blob/main/arduino/schema.png)


## :bulb: Running

1. Open up the terminal, navigate to the git folder, you just cloned, and run the following command:
```
$ python3 maskdetector.py
```
If you would like to use your Arduino, then append this flag: -a COM4 (number of comport)
```
$ python3 maskdetector.py -a COM4
```

Wait for the program to start. If everything was succesfull, then you will see the preview of your webcam, and the program will display your mask-wearing-status.

## Showcase video
https://www.youtube.com/watch?v=eLyNWEL1Los

## 🖥️ Used libraries

- [OpenCV](https://opencv.org/)
- [Caffee-based face recognition engine](https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/resnet_ssd_face_python.py)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

## TODO:
  * Thermometry
  * More ideas can come in a pull request :)

## 🎉 Thanks for reading
If you have any problem with this program, then contact me in email: `fegyverdavid.bator@gmail.com`, or open an issue here: [Szabadfogasu-maszk](https://github.com/davidfegyver/szabadfogasu-maszk/issues)


## :handshake: Contribution
If you got any idea, or you want to fix a bug, then please open a **Pull request**.

Contributors:
- [Fegyver Dávid](https://github.com/davidfegyver)
- [PiciAkk](https://github.com/piciakk)

**If you liked the project, give me a star :D**

## 📝 License

**MIT**
https://choosealicense.com/licenses/mit/
