import RPi.GPIO as gpio
from time import sleep


gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)


gpio.setup(22, gpio.OUT)                 # Stepper motor pins
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(26, gpio.OUT)

def LocknLoad(Debug, dartrdy):                        # Dart is laoded to the chamber ready to shoot
        
        #stepper motor control here
        if Debug == True:
            if dartrdy == True:
                print("dartrdy is ", dartrdy)