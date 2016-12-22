import time
import picamera
import shutil
import os
from ultimate_gps import *
from imu import *

camera = picamera.PiCamera()

def return_picture_name ():
    imu_data=imu_current_value()
    file_type=".jpg"
    picture_name= imu_data+file_type
    return picture_name

def set_exif():
    global camera 
    gps=gps_current_value ()
    if gps != "gps not fixed":
        camera.exif_tags['EXIF.GPSLatitude']= float(gps[0:5])  ## CHEK, Use 3 rationals degrees, minures, and seconds dd/1, mm/1, ss/1
        camera.exif_tags['EXIF.GPSLongitude']= float(gps[6:11])  ## CHECK
    imu_data=imu_current_value()
    camera.exif_tags['EXIF.UserComment']=imu_current_value()

def camera_take_picture():
    set_exif()
    global camera
    camera.capture(return_picture_name())
    #shutil.copy(/tmp/stream/pic.jpg,Desktop/bla.jpg)

def camera_begin_stream():
    os.system("sudo ./livestream.sh")
        
if __name__ == '__main__':
    camera_take_picture()
    
