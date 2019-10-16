import tyres as ty                  # Includes tyre movements
import camera as cam                # Includes camera functions

camOK = False                       # setup booleans, always False at start
motor = False
servos = False
dartrdy = False



DartCount = 1                       # Dart counter, in this solution max dart count is 3


# Alustus
# Kameran tarkistus
# Ajo- ja ampumamoottoreiden tarkistus
# Servot nollaan
# Magneettirele


# def renkaat
# Rengasfunktio 
# Tehty

# def servot
# Määritykset tähtäykseen

# def lataa
# Moottorit taakse
# Monesko tikka? Jos 2. tai 3 niin stepper

# def Laukaisu
# Moottorit eteen
# Solenoidi purskaus
# Lähtikö?

# def lopetus
# Jos kolmas tikka
# ???


def main():
    print("setup")
    if camOK == False or motor == False or servos == False:
        
        setup()
    
    else:                              # Shooting happens only if camera and motors are ok
        if DartCount < 4:              # and Dart count is lower than 4, meaning 1, 2, or 3
            if dartrdy == False:
                LocknLoad()
            if dartrdy == True: 
                FireAtWill()
        else:                          # if DartCount would be 4, or anything else shooting won't happen
            ShutDown()







          

def setup():                            #Returns booleans as True if camera and motors are ok and in position 
    if camcheck == 1:                   #check for camera
        camOK = True
        return camOK

    if motorcheck == 1:                 #check for DC motors
        motor = True
        return motor
    if servocheck == 1:                 #check for Servo motors and resetting them to original position
        servos = True
        return servos


def servomvmnt(): #Turret turn
    
     #Servo movement config
     servo = servo


def LocknLoad():                        # Dart is laoded to the chamber ready to shoot

    DartCount = DartCount + 1           # Dart counter, shooting stops after dart number 3 
    return DartCount

    if DartCount < 4:
        motor1 = 0                      # Motors are spun backwards to make sure that there is no misfire
        motor2 = 1
        time.sleep(5)
        dartrdy = True                 # After loading is done return ready state for fireing
        return dartrdy

    if DartCount == 4:
        ShutDown()

    
def FireAtWill():                       # Shooting function
      if DartCount < 4 and dartrdy == True:
          motor1 = 1                    # Motors are spun in advance to have them at full speed before fireing
          motor2 = 0
          time.sleep(5)
          solenoid = 1                  # After waiting 5 seconds solenoid burst will fire the dart
          dartrdy = False
          return dartrdy



def ShutDown():                         # After successfully fired 3 darts
    # DOES WHATEVER DARTBOT DOES
    loppu == loppu
