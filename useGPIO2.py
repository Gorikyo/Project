# Write your code here :-)
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4,GPIO.LOW)

state= GPIO.input(4)

print("state", state)

#GPIO.cleanup()
