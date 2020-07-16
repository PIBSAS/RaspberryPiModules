import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
Pin_Signal = 24
GPIO.setup(Pin_Signal, GPIO.OUT, initial = GPIO.LOW)
  
print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

try:
    while True:
        print("LED encendido por 4 segundos")
        GPIO.output(Pin_Signal, GPIO.HIGH)
        time.sleep(4)
        print("LED apagado por 2 segundos") 
        GPIO.output(Pin_Signal, GPIO.LOW)
        time.sleep(2)

except KeyboardInterrupt:
        GPIO.cleanup()