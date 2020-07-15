import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
GPIO_Pin_Signal = 24

GPIO.setup(GPIO_Pin_Signal,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
  
print("Prueba de modulo [Presiona Ctrl + C para finalizar la prueba]")

def funcionSalida(null):
        print("Ha sido detectado")
  
GPIO.add_event_detect(GPIO_Pin_Signal,GPIO.RISING,callback = funcionSalida,bouncetime = 100) 
  
# loop
try:
        while True:
                time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()