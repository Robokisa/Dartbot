import RPi.GPIO as gpio
import solenoid as sol
from time import sleep
gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)               # Launch motor pin



def FireAtWill(Debug, dartrdy, DartCount):                       # Shooting function
        gpio.output(7, True)
          
        if Debug == True:    
            if gpio.input(7):
                print("port 7 is HIGH")
                  
        sleep(5)
        sol.solenoidburst(Debug)           # After waiting 5 seconds solenoid burst will fire the dart

        gpio.output(7, False)
          
        if Debug == True:    
            if not gpio.input(7):
                print("port 7 is LOW")
                
        
        if Debug == True:
            print("dartrdy is ", dartrdy)
            print("DartCount is ", DartCount)
