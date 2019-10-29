import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)

control_pins = [7,11,13,15]
for pin in control_pins:
    gpio.setup(pin, gpio.OUT)
    #gpio.output(pin, 0)
    halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]
def steppermotor(): 
    for i in range(200):
        for halfstep in range(8):
            for pin in range(4):
                gpio.output(control_pins[pin],halfstep_seq[halfstep][pin])
                print(control_pins[pin],halfstep_seq[halfstep][pin])
