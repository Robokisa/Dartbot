import RPi.GPIO as gpio
from time import sleep

M1 = 21
M2 = 19
M3 = 18
M4 = 16

gpio.setmode(gpio.BOARD)

gpio.setup(M1, gpio.OUT)
gpio.setup(M2, gpio.OUT)
gpio.setup(M3, gpio.OUT)
gpio.setup(M4, gpio.OUT)

def eteen():
        gpio.output(M1, False)
        gpio.output(M2, True) 
        gpio.output(M3, True)
        gpio.output(M4, False)
        sleep(2)

def taakse():
    gpio.output(M1, True)
    gpio.output(M2, False)
    gpio.output(M3, False)
    gpio.output(M4, True)
    sleep(2)

def vasemmalle():
    gpio.output(M1,  True)
    gpio.output(M2, False)
    gpio.output(M3, True )
    gpio.output(M4, False)
    sleep(2)

def oikealle():
    gpio.output(M1,  False)
    gpio.output(M2, True)
    gpio.output(M3, False)
    gpio.output(M4, True)
    sleep(2)


