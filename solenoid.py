import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(11, gpio.OUT)

def solenoidburst():
    
    gpio.output(11, True)
    sleep(1)
    gpio.output(11, False)
    
    gpio.cleanup()
    