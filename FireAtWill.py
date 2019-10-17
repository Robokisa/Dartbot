import RPi.GPIO as gpio

GPIO.setmode(GPIO.BOARD)

motor1 = gpio.setup(PINNI??, gpio.OUT)
motor2 = gpio.setup(PINNI??, gpio.OUT)

def FireAtWill():                       # Shooting function
      if DartCount < 4 and dartrdy == True:
          gpio.output(M1, False)
          gpio.output(M2, True) 
          time.sleep(5)
          sol.solenoidburst()                  # After waiting 5 seconds solenoid burst will fire the dart
          dartrdy = False
          return dartrdy


