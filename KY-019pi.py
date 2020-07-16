import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
retraso = 1
Pin_S = 24

GPIO.setup(Pin_S, GPIO.OUT)
GPIO.output(Pin_S, False)

print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

try:
    while True:
        GPIO.output(Pin_S, True)
        time.sleep(retraso)
        GPIO.output(Pin_S, False)
        time.sleep(retraso)

except KeyboardInterrupt:
    GPIO.cleanup()