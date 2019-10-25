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

def taakse():
    gpio.output(M1, True)
    gpio.output(M2, False)
    gpio.output(M3, False)
    gpio.output(M4, True)

def vasemmalle():
    gpio.output(M1,  True)
    gpio.output(M2, False)
    gpio.output(M3, True )
    gpio.output(M4, False)

def oikealle():
    gpio.output(M1,  False)
    gpio.output(M2, True)
    gpio.output(M3, False)
    gpio.output(M4, True)

def carTurnO():
    #oikealle 90 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnV():
    #vasemmalle 90 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
def carTurnO120():
    #oikealle 20 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnO140():
    #oikealle 40 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnO160():
    #oikealle 60 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnV20():
    #vasemmalle 20 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
def carTurnV40():
    #vasemmalle 40 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
 def carTurnV60():
    #vasemmalle 60 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
   
   
  
    
