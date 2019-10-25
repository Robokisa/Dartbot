
from adafruit_servokit import ServoKit
import tyres as ty

kit = ServoKit(channels=16)


def readservo():

    if kit.servo[14].angle <95 and >85:
        eteen()

    elif kit.servo[14].angle <180 and >160:
        carTurnO()

    elif kit.servo[14].angle <20 and >0:
        carTurnV()

    elif kit.servo[14].angle <40 and >20:
        carTurnV60()

    elif kit.servo[14].angle <60 and >40:
        carTurnV40()

    elif kit.servo[14].angle <85 and >60:
        carTurnV20()

    elif kit.servo[14].angle <120 and >95:
        carTurnO20()

    elif kit.servo[14].angle <140 and >120:
        carTurnO40()

    elif kit.servo[14].angle <160 and >140:
        carTurnO60()

    sleep(1,5)




        



