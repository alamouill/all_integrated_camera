import time
import picamera
import shutil

def return_picture_name ():
    gps_data="Lat26.3,Long:46.12"
    imu_data="r:123,p:345,y:354"
    file_type=".jpg"
    picture_name= gps_data+imu_data+file_type
    return picture_name

def camera_take_picture():
    #camera=picamera.PiCamera()
    #camera.capture(return_picture_name())
    shutil.copy(/tmp/stream/pic.jpg,Desktop/bla.jpg)
    
    
if __name__ == '__main__':
    camera_take_picture()
    
