import tyres as ty                  # Includes tyre movements
#import camera as cam                # Includes camera functions
import solenoid as sol              # Function for solenoid burst, "trigger"
import FireAtWill as fire           # Launch function
import LocknLoad as load            # Load function
import RPi.GPIO as gpio
#import stepper_motor as step

import setupfile

from time import sleep

Debug = True

camOK = False                       # setup booleans, always False at start
motor = False
servos = False

dartrdy = False

DartCount = 1 
                      # Dart counter, in this solution max dart count is 3



def main_move():
    if camOK == 0:     # Camera sends constant data about target, if not found car turns 90 degrees
        servosweep()   # at a time and does new servo sweep to find the target
            if camOK == 0:
                while camOK == 0:
                    carTurn()
                    servosweep()
    
    if camOK == 1:    # once camera finds the target the car will be moved to 90 degree angle
        readServo()
        #LIIKUTETAAN AUTOA SERVON PERUSTEELLA
        
        if angleOK == 1:  # Once the angle is 90 degrees range is measured
            readServo()   # and car is moved accordingly
            #käännä auto oikein päin
            #Liikutetaan eteen tai taakse
        
            if rangeOK == 1: # When range is ok the fire command will be given
                fireOK = 1:


def main_fire():
    global Debug
    global DartCount                             # Shooting happens only if camera and motors are ok
    global dartrdy
    if DartCount < 4:              # and Dart count is lower than 4, meaning 1, 2, or 3

        if dartrdy == False:
            dartrdy = True
            load.LocknLoad(Debug, dartrdy)
        
        if dartrdy == True:
            dartrdy = False
            fire.FireAtWill(Debug, dartrdy, DartCount)
            DartCount = DartCount + 1
            sleep(5)
    else:                          # if DartCount would be 4, or anything else shooting won't happen
        ShutDown()
    




            




def setup():                            #Returns booleans as True if camera and motors are ok and in position 
    if camcheck == 1:                   #check for camera
        camOK = True
        return camOK


def ShutDown():                         # After successfully fired 3 darts
    # DOES WHATEVER DARTBOT DOES
    while(1):
        print("DartCount is ", DartCount)
        print("LOPPU")
        sleep(1000000)

if fireOK == 1:
    main_fire()
else fireOK == 0:
    main_move()

