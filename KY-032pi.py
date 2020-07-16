import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO_Pin_Signal = 24
GPIO.setup(GPIO_Pin_Signal, GPIO.IN, pull_up_down = GPIO.PUD_UP)

retraso = 0.5
 
print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

try:
    while True:
        if GPIO.input(GPIO_Pin_Signal) == True:
            print("Sin obstaculo")
        else:
            print("Obstaculo detectado")
            
        time.sleep(retraso)
 
except KeyboardInterrupt:
        GPIO.cleanup()