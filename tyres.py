import RPi.GPIO as gpio
import time

MO = 12
MV = 13


gpio.setmode(gpio.BOARD)

gpio.setup(MO, gpio.OUT)
gpio.setup(MV, gpio.OUT)

eteen()


def eteen():
    gpio.output(MO, True)
    gpio.output(MV, True) 
    sleep(5)

def vasemmalle():
    gpio.output(MO,  True)
    gpio.output(MV, False)
    

def oikealle():
    gpio.output(MO,  False)
    gpio.output(MV, True)
   

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
    
   
   
  
    
