# camera.py

import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
	self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#Establecemos el rango de colores que vamos a detectar
	#En este caso de verde oscuro a verde-azulado claro
	verde_bajos = np.array([49,50,50], dtype=np.uint8)
	verde_altos = np.array([80, 255, 255], dtype=np.uint8)
        azul_bajos = np.array([100,50,50], dtype=np.uint8)
        azul_altos = np.array([130, 255, 255], dtype=np.uint8)

	#Crear una mascara con solo los pixeles dentro del rango de verdes
	mask = cv2.inRange(hsv, verde_bajos, verde_altos)
	#Crear una mascara con solo los pixeles dentro del rango de azules
        mask1 = cv2.inRange(hsv, azul_bajos, azul_altos)
	
	#Encontrar el area de los objetos que detecta la camara verdes
	moments = cv2.moments(mask)
	area = moments['m00']
        #Encontrar el area de los objetos que detecta la camara azules
        moments1 = cv2.moments(mask1)
        area1 = moments1['m00']
 
	#Descomentar para ver el area por pantalla
#        print "verde = ", area
#        print "azul = ", area1

	if(area > 2000000 and area1 > 2000000):
	#Buscamos el centro x, y del objeto verde
		x = int(round(moments['m10']/moments['m00']))
	        y = int(moments['m01']/moments['m00'])
	#Buscamos el centro x, y del objeto azul
                x1 = int(round(moments1['m10']/moments1['m00']))
                y1 = int(moments1['m01']/moments1['m00'])
         
        #Mostramos sus coordenadas por pantalla
	        print "XV=", x," YV=", y," XA=", x1," YA=", y1
#	        print "YV = ", y
#		print "XA = ", x1
#                print "YA = ", y1
 
        #Dibujamos una marca en el centro del objeto
	        cv2.rectangle(image, (x, y), (x+2, y+2),(0,0,255), 2)        
        #Dibujamos una marca en el centro del objeto
                cv2.rectangle(image, (x1, y1), (x1+2, y1+2),(0,0,255), 2)

#        if(area1 > 2000000):
        #Buscamos el centro x, y del objeto
#                x1 = int(round(moments1['m10']/moments1['m00']))
#                y1 = int(moments1['m01']/moments1['m00'])
 
        #Mostramos sus coordenadas por pantalla
#                print "XA = ", x1
#                print "YA = ", y1

        #Dibujamos una marca en el centro del objeto
#                cv2.rectangle(image, (x1, y1), (x1+2, y1+2),(0,0,255), 2)
	# We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
#	print("XV", x, "YV", y, "XA", x1,"YA", y1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()
