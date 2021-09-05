#import required libraries
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


from imutils.video import VideoStream

import numpy as np
import argparse
import imutils
import serial
import time
import cv2
import os

import flask
import threading
from flask import request, jsonify

# declare maskStatus json
maskStatus = {}
# define the webserver thread
def webServer():
    app = flask.Flask(__name__)
    @app.route('/', methods=['GET'])
    def webAPI():
        return jsonify(maskStatus)

    app.run(port=webServerPort)

# check command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--arduino","-a", dest='COM', help="The COM port of the arduino, ex: com4")
parser.add_argument("--port", "-p", dest="PORT", help="Define the port of the web API (default: 5000)")
parser.add_argument("--ipcam", "-ip", dest="IP", help="The URL of the IP Camera ()")
args = parser.parse_args()

#import serial and start serial communication
webServerPort = args.PORT or 5000
if args.COM is not None:
	s = serial.Serial(args.COM, 9600, timeout=5)
# start the webserver thread
webServerThread = threading.Thread(target=webServer)
webServerThread.start()

#Simple logger library :D
class Logger:
	def info(self,text,idk = False):
		print('\033[94m [INFO] '+text+'\033[0m',end='' if idk else '\n')
	def ok(self,text,idk = False):
		print('\033[92m [OK] '+text+'\033[0m',end='' if idk else '\n')
	def warn(self,text,idk = False):
		print('\033[93m [WARN] '+text+'\033[0m',end='' if idk else '\n')
	def fail(self,text,idk = False):
		print('\033[91m [FAIL] '+text+'\033[0m',end='' if idk else '\n')
logger = Logger()

#Loading things up
logger.info("Loading Face Detector... ",True)
faceDetector = cv2.dnn.readNet("./face_detector/deploy.prototxt", "./face_detector/res10_300x300_ssd_iter_140000.caffemodel")
logger.ok("Done")


logger.info("Loading Mask Detector... ")
paths = [os.path.join("./models", path) for path in os.listdir("./models")]
latest = sorted(paths, key=os.path.getmtime)[-1]

logger.info(f"Latest model path: {latest}")
maskDetector = load_model(latest)
logger.ok("Done")


logger.info("Starting video capture...",True)
vs = VideoStream(src=args.IP or 0).start()
time.sleep(2.0)
logger.ok("Done")

#check starting time for fps counting
start = time.time()

while True:

	frame=vs.read() #read the camera
	if frame is None:
		logger.warn("The video frame is None. Check your input.")
		time.sleep(1)
		continue

	frame = imutils.resize(frame, width=400) # resize for better fps

	(height, width) = frame.shape[:2]


	blob = cv2.dnn.blobFromImage(frame, 1.0, (300,300), (104.0, 177.0, 123.0)) 	#make a blob from the camera pic for the face detector

	#pass the blob through the network
	faceDetector.setInput(blob)
	detections = faceDetector.forward()

	faces = []
	locations = []
	predictions = []


	#process the faces to arrays
	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]

		if confidence > 0.5:
			(startX, startY, endX, endY) = np.multiply(
				detections[0, 0, i, 3:7],
				[width, height, width, height]
			).astype("int") #get the bounding box of the face

			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(width - 1, endX), min(height - 1, endY))

			#grab the face and convert to rgb (because the predictor can only process rgb)
			#and resize it
			face = frame[startY:endY, startX:endX]
			try:
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			except:
				logger.warn("!_src.empty() -- Check your input.")
				continue
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)


			faces.append(face)
			locations.append((startX, startY, endX, endY))

	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		predictions = maskDetector.predict(faces, batch_size=32)
	else:
		if args.COM is not None:
			s.write('2'.encode())

	#show fps
	fps_str = "FPS: %.2f" % (1 / (time.time() - start))
	start = time.time()
	cv2.putText(frame, fps_str, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,0, 0), 2)

	#loop through all faces and add it to the end photo
	for (box, preds) in zip(locations, predictions):
		(aX, aY, bX, bY) = box
		(mask, withoutMask) = preds

		havemask = mask > withoutMask
		if havemask:
			label = "Mask"
			color = (0, 255, 0)
			maskStatus = {
				"faces": zip(locations, predictions),
				"prettyStatus": "Wearing mask",
				"shortStatus": True
			}
		else:
			label = "No Mask"
			color = (0, 0, 255)
			maskStatus = {
				"faces": zip(locations, predictions),
				"prettyStatus": "Not wearing mask",
				"shortStatus": False
			}

		#send data to arduino
		if args.COM is not None:
			s.write('1' if havemask else '0'.encode())

		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		cv2.putText(frame, label, (aX, aY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.40, color, 2)
		cv2.rectangle(frame, (aX, aY), (bX, bY), color, 2)


	#show the frame
	cv2.imshow("Mask Detector by davidfegyver", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
