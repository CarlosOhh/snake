# main.py
from RPIO import PWM 
import time
import atexit
from flask import Flask, render_template, Response, request
from camera_test import VideoCamera

app = Flask(__name__)


# This function maps the angle we want to move the servo to, to the needed PWM value
def PanMap(angle):
	return int((round((770.0/180.0),0)*angle) +330)

#def TiltMap(angle):
#        return int((round((400.0/180.0),0)*angle) +300)

# Create a dictionary called pins to store the pin number, name, and angle
pins = {
    2 : {'name' : 'pan', 'angle' : 90},
    3 : {'name' : 'tilt', 'angle' : 90}
    }

# Create two servo objects using the RPIO PWM library
servoPan = PWM.Servo()
servoTilt = PWM.Servo()

# Setup the two servos and turn both to 90 degrees
servoPan.set_servo(2, PanMap(90))
servoPan.set_servo(3, PanMap(90))

# Cleanup any open objects
def cleanup():
    servo.stop_servo(3)
    servo.stop_servo(2)

@app.route('/')
def index():
    return render_template('index3.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# The function below is executed when someone requests a URL with a move direction
@app.route("/<direction>")
def move(direction):
    # Choose the direction of the request
    if direction == 'left':
	    # Increment the angle by 10 degrees
        na = pins[2]['angle'] + 10
        # Verify that the new angle is not too great
        if int(na) <= 170:
            # Change the angle of the servo
            servoPan.set_servo(2, PanMap(na))
            # Store the new angle in the pins dictionary
            pins[2]['angle'] = na
	print na
        return str(na) + ' ' + str(PanMap(na))
    elif direction == 'right':
        na = pins[2]['angle'] - 10
        if na >= 10:
            servoPan.set_servo(2, PanMap(na))
            pins[2]['angle'] = na
        print na
        return str(na) + ' ' + str(PanMap(na))
    elif direction == 'down':
        na = pins[3]['angle'] + 10
        if na <= 170:
            servoTilt.set_servo(3, PanMap(na))
            pins[3]['angle'] = na
        print na
        return str(na) + ' ' + str(PanMap(na))
    elif direction == 'up':
        na = pins[3]['angle'] - 10
        if na >= 30:
            servoTilt.set_servo(3, PanMap(na))
            pins[3]['angle'] = na
        print na
        return str(na) + ' ' + str(PanMap(na))

# Function to manually set a motor to a specific pluse width
@app.route("/<motor>/<pulsewidth>")
def manual(motor,pulsewidth):
    if motor == "pan":
        servoPan.set_servo(2, int(pulsewidth))
    elif motor == "tilt":
        servoPan.set_servo(3, int(pulsewidth))
    return "Moved"

# Clean everything up when the app exits
atexit.register(cleanup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
