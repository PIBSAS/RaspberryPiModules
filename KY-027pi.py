import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 24
Pin_L = 23

GPIO.setup(Pin_L, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

def funcionMagic(null):
    GPIO.output(LED,True)
    
GPIO.add_event_detect(Pin_L, GPIO.FALLING, callback=funcionMagic, bouncetime = 10)

try:
    while True:
        time.sleep(1)
        if GPIO.input(Pin_L):
            GPIO.output(LED, False)

except KeyboardInterrupt:
    GPIO.cleanup()