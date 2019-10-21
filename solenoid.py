import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)


def solenoidburst(Debug):
    
    gpio.output(11, True)
    
    if Debug == True:
        if gpio.input(11):
            print("11 is HIGH")
            
    sleep(1)
    
    gpio.output(11, False)
    
    if Debug == True:
        if not gpio.input(11):
            print("11 is low")