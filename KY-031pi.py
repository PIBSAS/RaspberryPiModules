import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_Pin_Signal = 24
GPIO.setup(GPIO_Pin_Signal, GPIO.IN)

print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

def funcionDetectar(null):
    print("Ha sido detectado")
    
GPIO.add_event_detect(GPIO_Pin_Signal, GPIO.FALLING,callback = funcionDetectar, bouncetime = 100)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()