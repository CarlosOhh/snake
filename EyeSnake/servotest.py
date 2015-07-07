from RPIO import PWM          #import the library for PWM
import time                   #import time for pauses
servo=PWM.Servo()             #initialize the servo library
servo.set_servo(2,400)       #center the MG90S
time.sleep(2)
#for _i in range(3):          #loop between -90 and 90 degrees
#    servo.set_servo(2,2400)
#    time.sleep(1)
#    servo.set_servo(2,700)
#    time.sleep(1)
servo.set_servo(2,1000)
time.sleep(2)
