import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
Pin_S = 18
GPIO.setup(Pin_S,GPIO.OUT,initial = GPIO.LOW)

print("Prueba de modulo [Presiona Ctrl+C para finalizar la prueba]")

try:
    while True:
        print("Buzzer sonara por 4 segundos")
        GPIO.output(Pin_S,GPIO.HIGH)
        time.sleep(4)
        print("Buzzer no suena por 4 segundos")
        GPIO.output(Pin_S,GPIO.LOW)
        time.sleep(4)
        
except KeyboardInterrupt:
    GPIO.cleanup()