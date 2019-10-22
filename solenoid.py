import RPi.GPIO as gpio
from time import sleep

Debug = True
gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)


def solenoidburst(Debug):
    
    gpio.output(11, True)      # solenoid is given a burst to send the dart in motion
    
    if Debug == True:
        if gpio.input(11):
            print("11 is HIGH")
            
    sleep(5)
    
    gpio.output(11, False)
    
    if Debug == True:
        if not gpio.input(11):
            print("11 is low")

solenoidburst(Debug)