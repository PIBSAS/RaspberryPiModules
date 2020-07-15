import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
 
LED_Rojo = 22
LED_Verde = 24
LED_Azul = 16
 
GPIO.setup(LED_Rojo, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Verde, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Azul, GPIO.OUT, initial = GPIO.LOW)

print("Prueba de LED [Presiona Ctrl + C para finalizar la prueba]")
  
# loop
try:
        while True:
            print("LED Rojo se enciende durante 3 segundos")
            GPIO.output(LED_Rojo,GPIO.HIGH)         
            GPIO.output(LED_Verde,GPIO.LOW)      
            GPIO.output(LED_Azul,GPIO.LOW)         
            time.sleep(3)                                                     
            print("LED Verde se enciende durante 3 segundos") 
            GPIO.output(LED_Rojo,GPIO.LOW)          
            GPIO.output(LED_Verde,GPIO.HIGH)     
            GPIO.output(LED_Azul,GPIO.LOW)         
            time.sleep(3)                                                     
            print("LED Azul se enciende durante 3 segundos") 
            GPIO.output(LED_Rojo,GPIO.LOW)         
            GPIO.output(LED_Verde,GPIO.LOW)      
            GPIO.output(LED_Azul,GPIO.HIGH)       
            time.sleep(3)                                                   

except KeyboardInterrupt:
        GPIO.cleanup()