from servo import *
from camera import *
from ultimate_gps import *
from imu import *
from flask import Flask, render_template, request, Markup, Response
app = Flask(__name__)
import time
import math
import wiringpi



# Load the main form template on webrequest for the root page
@app.route("/")
def main():
    # to send any data to the template
    imu=imu_current_value()
    gps=gps_current_value ()
    # Pass the template data into the template picam.html and return it to the user
    return render_template('webinterface.html',imu=imu, gps=gps)#**templateData,,

# The function below is executed when someone requests a URL with a move direction
@app.route("/<direction>")
def move(direction):
    # Choose the direction of the request
    if direction == 'left':
        servo_pan_left()
    elif direction == 'right':
        servo_pan_right()
    elif direction == 'up':
        servo_tilt_up()
    elif direction == 'down':
        servo_tilt_down()
    elif direction == 'takepicture':
        camera_take_picture()
    elif direction == 'toorigin':
        print('GoingBack to origin...')
    elif direction == 'leftT':
        print('Going left')
        #thymio_go_left()
    elif direction == 'rightT':
        print('Going right')
        #thymio_go_right()
    elif direction == 'front':
        print('Going straight')
        #thymio_go_straight()
    elif direction == 'back':
        print('Going back')
        #thymio_go_backward()
    return 'OK'

#Update IMU and GPS displaying
@app.route('/<sensor_read>')
def update_sensor():
    return 'ok'



if __name__ == "__main__":
    init_servo()
 #   init_imu()
    init_gps()
#    camera_begin_stream()
    app.run(host='0.0.0.0', port=8000, debug=True)

