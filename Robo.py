import tyres as ty                  # Includes tyre movements
#import camera as cam                # Includes camera functions
import solenoid as sol              # Function for solenoid burst, "trigger"
import FireAtWill as fire           # Launch function
import LocknLoad as load            # Load function
import RPi.GPIO as gpio

from time import sleep

Debug = True

camOK = False                       # setup booleans, always False at start
motor = False
servos = False

dartrdy = False

DartCount = 1 
                      # Dart counter, in this solution max dart count is 3


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
    global Debug
    global DartCount                             # Shooting happens only if camera and motors are ok
    global dartrdy
    if DartCount < 4:              # and Dart count is lower than 4, meaning 1, 2, or 3

        if dartrdy == False:
            dartrdy = True
            load.LocknLoad(Debug, dartrdy)
        
        if dartrdy == True:
            dartrdy = False
            fire.FireAtWill(Debug, dartrdy, DartCount)
            DartCount = DartCount + 1
    else:                          # if DartCount would be 4, or anything else shooting won't happen
        ShutDown()
    




            




def setup():                            #Returns booleans as True if camera and motors are ok and in position 
    if camcheck == 1:                   #check for camera
        camOK = True
        return camOK


def ShutDown():                         # After successfully fired 3 darts
    # DOES WHATEVER DARTBOT DOES
    while(1):
        print("DartCount is ", DartCount)
        print("LOPPU")
        sleep(1000000)

while(1):
    main()