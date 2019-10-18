import RPi.GPIO as gpio
import solenoid as sol
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(6, gpio.OUT)               # Launch motor pin

Fire = False

def FireAtWill():                       # Shooting function
          gpio.output(6, True)
          sleep(5)
          sol.solenoidburst()           # After waiting 5 seconds solenoid burst will fire the dart

          gpio.output(6, False)
          dartrdy = False
          
          DartCount = DartCount + 1
          gpio.cleanup()