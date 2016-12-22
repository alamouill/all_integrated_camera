# Servo Control
import time
import math
import wiringpi

#initiate previous angle
prev_angle2 = 0
angle1=0
increment=10
def init_servo () : 
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()
     
    # set #18 to be a PWM output
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
    # set #19 to be a PWM output
    wiringpi.pinMode(19, wiringpi.GPIO.PWM_OUTPUT)
     
    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

     
    # divide down clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)
     
    delay_period = 0.01
    print ("Servo initialises")
     

def set_tilt (angle1=0):
    #checks that angle is within the range
    if angle1>180:
        print ('angle to big, setting to 180')
        angle1 = 180
    elif angle1 < 0:
        print ('angle too small, setting to 0')
        angle1 = 0

    #calculate pluse width
    pulse1 = int(angle1*1.05555+55) 
    wiringpi.pwmWrite(19, pulse1)

def servo_tilt_up ():
    #calculate pluse width
    global angle1
    global increment
    angle1+=increment
    if angle1>180:
        print ('angle to big, setting to 180')
        angle1 = 180
    pulse1 = int(angle1*1.05555+55) 
    wiringpi.pwmWrite(19, pulse1)

def servo_tilt_down ():
    #calculate pluse width
    global angle1
    global increment
    angle1-=increment
    if angle1<0:
        print ('angle to small, setting to 0')
        angle1 = 0
    pulse1 = int(angle1*1.05555+55) 
    wiringpi.pwmWrite(19, pulse1)

def set_pan (angle2):
##    if angle>angle_max_pos:
##        print ('angle to big, setting %d', angle_max_pos)
##        angle = angle_max_pos
##    elif angle < angle_min_pos:
##        print ('angle too small, setting to %d', angle_min_pos)
##        angle = angle_min_pos
##    
    global prev_angle2
    #calculate the way to go
    diff_angle2= angle2-prev_angle2    
    prev_angle2=angle2

    #set the PWM width
    if diff_angle2>0:
        angle_per_sec=140  #355
        pulse2=156
        
    else:
        angle_per_sec= 156  #335
        pulse2=144
    
    #set the time during wich the PWM is differents than NO MOVE
    sleep2 = math.fabs(float(diff_angle2)/float(angle_per_sec))

    print ('Pulse= ',pulse2, ' Sleep= ',sleep2, 'diff_angle= ', diff_angle2)
    #set speed
    wiringpi.pwmWrite(18, pulse2)
    #wait
    time.sleep(sleep2)

    #stop
    wiringpi.pwmWrite(18, 150)

def servo_pan_left ():
    global prev_angle2
    global increment
    prev_angle2-=increment
    angle_per_sec=156
    pulse2=140
    #set the time during wich the PWM is differents than NO MOVE
    sleep2 = math.fabs(float(increment)/float(angle_per_sec))
    #set speed
    wiringpi.pwmWrite(18, pulse2)
    #wait
    time.sleep(sleep2)
    #stop
    wiringpi.pwmWrite(18, 150)

def servo_pan_right ():
    global prev_angle2
    global increment
    prev_angle2 +=increment
    angle_per_sec=140
    pulse2=160
    #set the time during wich the PWM is differents than NO MOVE
    sleep2 = math.fabs(float(increment)/float(angle_per_sec))
    #set speed
    wiringpi.pwmWrite(18, pulse2)
    #wait
    time.sleep(sleep2)
    #stop
    wiringpi.pwmWrite(18, 150)
    

if __name__ == '__main__':
    init_servo ()
    while (True) :
        #angle1 = input ('angle1:  ')
        #angle2 = input ('angle2:  ')
    
        #set_tilt(angle1)
        #set_pan (angle2)
        servo_pan_left()
        servo_tilt_up()
        time.sleep(2)
