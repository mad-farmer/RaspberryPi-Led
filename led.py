import RPi.GPIO as GPIO
import time
#IMPORTING LIBRARIES


GPIO.setmode(GPIO.BOARD)
# Use physical pin numbering

pin=11
GPIO.setup(pin, GPIO.OUT,initial=GPIO.LOW)
# Set pin 11 to be an output pin and set initial value to low (off)



while True:
    GPIO.output(pin,GPIO.HIGH) #Turn On
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW) #Turn Off
    time.sleep(1)

GPIO.output(pin,GPIO.LOW)
GPIO.cleanup()


