#import required libraries
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


from imutils.video import VideoStream

import numpy as np
import imutils
import time
import cv2
import os
#import serial and start serial communication
arduino = True if input("Van arduinod? (i/n)")=='i' else False
if arduino:
	import serial
	s = serial.Serial(input("Arduino portja"), 9600, timeout=5) 

#Simple logger library :D 
class logger:
    INFO = '\033[94m [INFO] '
    OK = '\033[92m [OK] '
    WARNING = '\033[93m [WARN] '
    FAIL = '\033[91m [FAIL] '
    END = '\033[0m'

#Loading things up
print(logger.INFO+"Loading Face Detector... "+logger.END,end="")
faceDetector = cv2.dnn.readNet("./face_detector/deploy.prototxt", "./face_detector/res10_300x300_ssd_iter_140000.caffemodel")
print(logger.OK+"Done"+logger.END)


print(logger.INFO+"Loading Mask Detector... "+logger.END)
paths = [os.path.join("./models", path) for path in os.listdir("./models")]
latest = sorted(paths, key=os.path.getmtime)[-1]
print(logger.INFO+f"Latest model path: {latest}"+logger.END)
maskDetector = load_model(latest)
print(logger.OK+"Done"+logger.END)


print(logger.INFO+"Starting video capture..."+logger.END,end="")
vs = VideoStream(src=0).start()
time.sleep(2.0)
print(logger.OK+"Done"+logger.END)

#check starting time for fps counting
start = time.time()
while True:
	frame=vs.read() #read the camera
	frame = imutils.resize(frame, width=400) # resize for better fps

	#make a blob from the camera for the face detector
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))

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

			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			#grab the face and convert to rgb (because the predictor can only process rgb)
			#and resize it
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)


			faces.append(face)
			locations.append((startX, startY, endX, endY))

	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		predictions = maskDetector.predict(faces, batch_size=32)
	else:
		if arduino:
			s.write('2'.encode())
	#show fps
	fps_str = "FPS: %.2f" % (1 / (time.time() - start))
	start = time.time()
	cv2.putText(frame, fps_str, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,0, 0), 2)

	#loop through all faces and add it to the end photo
	for (locs, preds) in zip(locations, predictions):
		(aX, aY, bX, bY) = locs
		(mask, withoutMask) = preds

		havemask = mask > withoutMask

		label = "Mask" if havemask else "No Mask"
		color = (0, 255, 0) if havemask else (0, 0, 255)

		#send data to arduino
		if arduino:
			if havemask:
				s.write('1'.encode()) 
			else:
				s.write('0'.encode())
		
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
