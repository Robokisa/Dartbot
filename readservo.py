

import tyres as ty
from time import sleep

S1 = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(S1, GPIO.OUT)
pwm=GPIO.PWM(03, 50)


def SetAngle(angle):

	duty = angle / 18 + 2

	GPIO.output(S1, True)

	pwm.ChangeDutyCycle(duty)

	sleep(1)

	GPIO.output(S1, False)

	pwm.ChangeDutyCycle(0)




def readservo():

    if angle <95 and angle >85:
        eteen()

    elif angle <180 and angle >160:
        carTurnO()

    elif angle <20 and angle >0:
        carTurnV()

    elif angle <40 and angle >20:
        carTurnV60()

    elif angle <60 and angle >40:
        carTurnV40()

    elif angle <85 and angle >60:
        carTurnV20()

    elif angle <120 and angle >95:
        carTurnO20()

    elif angle <140 and angle >120:
        carTurnO40()

    elif angle <160 and angle >140:
        carTurnO60()
        
   
    sleep(1,5)
    
    




        



