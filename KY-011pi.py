import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
LED_Rojo = 16
LED_Verde = 18

GPIO.setup(LED_Rojo, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Verde, GPIO.OUT, initial = GPIO.LOW)
print("LED-Test [Presion ctrl+c para cerrar]")
  
# Main program loop
try:
        while True:
            print("LED Rojo se enciende por 3 segundos")
            GPIO.output(LED_Rojo,GPIO.HIGH)  
            GPIO.output(LED_Verde,GPIO.LOW) 
            time.sleep(3) 
            print("LED Verde se enciende por 3 segundos") 
            GPIO.output(LED_Rojo,GPIO.LOW) 
            GPIO.output(LED_Verde,GPIO.HIGH) 
            time.sleep(3) 
   
except KeyboardInterrupt:
        GPIO.cleanup()