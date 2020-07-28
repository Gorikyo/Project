# Write your code here :-)
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPOUT= [(2, "HIGH"), (3, "LOW"), (4,"HIGH")]

state=[]

for GP in GPOUT:
    GPIO.setup(GP[0], GPIO.OUT)
    if GP[1]=="HIGH":
        GPIO.output(GP[0],GPIO.HIGH)
    else:
        GPIO.output(GP[0],GPIO.LOW)

    print( (GP[0] ,GPIO.input(GP[0])) )
    state.append( (GP[0] ,GPIO.input(GP[0])) )
