
from adafruit_servokit import ServoKit
import tyres as ty

kit = ServoKit(channels=16)


def readservo():

    if kit.servo[1].angle <95 and kit.servo[1].angle >85:
        eteen()

    elif kit.servo[1].angle <180 and kit.servo[1].angle >160:
        carTurnO()

    elif kit.servo[1].angle <20 and kit.servo[1].angle >0:
        carTurnV()

    elif kit.servo[1].angle <40 and kit.servo[1].angle >20:
        carTurnV60()

    elif kit.servo[1].angle <60 and kit.servo[1].angle >40:
        carTurnV40()

    elif kit.servo[1].angle <85 and kit.servo[1].angle >60:
        carTurnV20()

    elif kit.servo[1].angle <120 and kit.servo[1].angle >95:
        carTurnO20()

    elif kit.servo[1].angle <140 and kit.servo[1].angle >120:
        carTurnO40()

    elif kit.servo[1].angle <160 and kit.servo[1].angle >140:
        carTurnO60()

    sleep(1,5)




        



