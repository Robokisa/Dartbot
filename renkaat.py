import RPi.GPIO as gpio

M1 = 02
M2 = 03
M3 = 04
M4 = 05

gpio.setup(M1, gpio.OUT)
gpio.setup(M2, gpio.OUT)
gpio.setup(M3, gpio.OUT)
gpio.setup(M4, gpio.OUT)

def eteen():
    gpio.output(M1, False)
    gpio.output(M2, True) 
    gpio.output(M3, True)
    gpio.output(M4, False)
    time.sleep()
    gpio.cleanup()

def taakse():
    gpio.output(M1, True)
    gpio.output(M2, False)
    gpio.output(M3, False)
    gpio.output(M4, True)
    time.sleep()
    gpio.cleanup()

    def vasemmalle():
    gpio.output(M1,  True)
    gpio.output(M2, False)
    gpio.output(M3, True )
    gpio.output(M4, False)
    time.sleep()
    gpio.cleanup()

def oikealle():
    gpio.output(M1,  False)
    gpio.output(M2, True)
    gpio.output(M3, False)
    gpio.output(M4, True)
    time.sleep()
    gpio.cleanup()


