from Tkinter import *
import time
import math
import wiringpi
from servo import *
from camera import *
from ultimate_gps import *
from imu import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Servo tilt').grid(row=0, column=0)
        Label(frame, text='Servo pan').grid(row=1, column=0)
        scaletilt = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.updatetilt)
        scaletilt.grid(row=0, column=1)
        scalepan = Scale(frame, from_=-180, to=180,
              orient=HORIZONTAL, command=self.updatepan)
        scalepan.grid(row=1, column=1)

        self.camera = Button(frame, text="Take Picture", command=self.take_photo)
        self.camera.grid(row=2, column=0)

        self.goleft = Button(frame, text="Go Left", command=self.go_left)
        self.camera.grid(row=2, column=1)

        label1 = Label(frame, text = gps_current_value ())
        label1.grid(row = 3, column =0)

        label2 = Label(frame, text = imu_current_value ())
        label2.grid(row = 3, column =1)


    def updatetilt(self, angle):
        set_tilt(int(angle))

    def updatepan(self, angle):
        set_pan(int(angle))

    def take_photo(self):
        camera_take_picture()

    def go_left(self):
        servo_pan_left()
        
        
	
def init_interface ():
    root = Tk()
    root.wm_title('All Integrated Camera fro outdoor rovers')
    app = App(root)
    root.geometry("200x150+0+0")
    root.mainloop()


if __name__ == '__main__':
    init_servo()
#    init_imu()
    init_gps()
    init_interface()
    
