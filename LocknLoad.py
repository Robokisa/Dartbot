import RPi.GPIO as gpio
from time import sleep

dartrdy = False

gpio.setmode(gpio.BCM)

gpio.setup(7, gpio.OUT)                 # Stepper motor pins
gpio.setup(8, gpio.OUT)
gpio.setup(9, gpio.OUT)
gpio.setup(10, gpio.OUT)

def LocknLoad():                        # Dart is laoded to the chamber ready to shoot
        
        #stepper motor control here
        
        dartrdy = True
        
        gpio.cleanup()