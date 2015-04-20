import serial
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write("\x06\x10\x46\x46")

ser.close()
