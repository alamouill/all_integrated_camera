import sys, getopt


sys.path.append('.')

import RTIMU
import os.path
import time
import math

imu = RTIMU.RTIMU(RTIMU.Settings("RTIMULib"))

def init_imu():
    global imu
    SETTINGS_FILE = "RTIMULib"
    print("Using settings file " + SETTINGS_FILE + ".ini")
    if not os.path.exists(SETTINGS_FILE + ".ini"):
        print("Settings file does not exist, will be created")

    s = RTIMU.Settings(SETTINGS_FILE)
    imu = RTIMU.RTIMU(s)

    print("IMU Name: " + imu.IMUName())

    if (not imu.IMUInit()):
        print("IMU Init Failed")
        sys.exit(1)
    else:
        print("IMU Init Succeeded")

    # Set fusion parameters

    imu.setSlerpPower(0.02)
    imu.setGyroEnable(True)
    imu.setAccelEnable(True)
    imu.setCompassEnable(True)

    poll_interval = imu.IMUGetPollInterval()
    print("Recommended Poll Interval: %dmS\n" % poll_interval)
    if imu.IMURead():
        # x, y, z = imu.getFusionData()
        # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
        print("In Init r: %f p: %f y: %f" , math.degrees(fusionPose[0]),math.degrees(fusionPose[1]), math.degrees(fusionPose[2]))
    else :
        print("No IMU Data in")
        return "Unable to Get IMU Data"
    

def imu_current_value():
    global imu
    if imu.IMURead():
        # x, y, z = imu.getFusionData()
        # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
        print("r: %f p: %f y: %f" , math.degrees(fusionPose[0]),math.degrees(fusionPose[1]), math.degrees(fusionPose[2]))
        return 'r'+str(math.degrees(fusionPose[0]))+'p'+str(math.degrees(fusionPose[1]))+'y'+str(math.degrees(fusionPose[2]))

    else :
        print("No IMU Data")
        return "Unable to Get IMU Data"

if __name__=='__main__':
    init_imu()
    while (True):
        imu_current_value()
        time.sleep(.5)
        
