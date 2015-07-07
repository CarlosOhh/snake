import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
	# Capture frame-by-frame
	ret, image = cap.read()
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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

    # Display the resulting frame
	cv2.imshow('frame',image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
