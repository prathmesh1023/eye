import numpy as np
import cv2
import glob

path = '/home/tejas/Desktop/Untitled Folder/pre/*.jpg'

face_cascade = cv2.CascadeClassifier('haarcascadefrontalfacedefault.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

files = glob.glob(path)
i = 1
for file in files:
	img = cv2.imread(file)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		#roi_gray = gray[y:y+h, x:x+w]
		#roi_color = img[y:y+h, x:x+w]
		#eyes = eye_cascade.detectMultiScale(roi_gray)
		#for (ex,ey,ew,eh) in eyes:
			#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	#cv2.imshow('img',img)
	path1 = '/home/tejas/Desktop/detected_face/pre/test'
	extention = '.jpeg'
	destination_path = '%s%d%s' % (path1, i, extention)
	i = i + 1
	cv2.imwrite(destination_path, img)
	#cv2.destroyAllWindows()