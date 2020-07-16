import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_Rojo = 6
LED_Verde = 5
LED_Azul = 4

GPIO.setup(LED_Rojo, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Verde, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Azul, GPIO.OUT, initial = GPIO.LOW)

print("Prueba de modulo [Presiona Ctrl + C para finalizar la prueba]")
try:
    while True:
        print("Led Rojo se enciende por 3 segundos")
        GPIO.output(LED_Rojo, GPIO.HIGH)
        GPIO.output(LED_Verde, GPIO.LOW)
        GPIO.output(LED_Azul, GPIO.LOW)
        time.sleep(3)
        print("Led Verde se enciende por 3 segundos")
        GPIO.output(LED_Rojo, GPIO.LOW)
        GPIO.output(LED_Verde, GPIO.HIGH)
        GPIO.output(LED_Azul, GPIO.LOW)
        time.sleep(3)
        print("Led Azul se enciende por 3 segundos")
        GPIO.output(LED_Rojo,GPIO.LOW)
        GPIO.output(LED_Verde,GPIO.LOW)
        GPIO.output(LED_Azul,GPIO.HIGH)
        time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()