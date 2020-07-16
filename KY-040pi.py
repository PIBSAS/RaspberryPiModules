import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_CLK = 16
PIN_DT = 15
PIN_SW = 14

GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_DT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
Contador = 0
direccion = True
PIN_CLK_anterior = 0
PIN_CLK_actual = 0
retraso = 0.01
PIN_CLK_anterior = GPIO.input(PIN_CLK)

def deteccionGiro(null):
    global Contador
    PIN_CLK_actual = GPIO.input(PIN_CLK)
    if PIN_CLK_actual != PIN_CLK_anterior:
        if GPIO.input(PIN_DT) != PIN_CLK_actual:
            Contador += 1
            direccion = True;
        else:
            direccion = False
            Contador = Contador - 1
        print("Rotacion detectada: ")
        if direccion:
            print("Sentido horario")
        else:
            print("Sentido anti-horario")
        print("Posicion actual: ",Contador)

def resetContador(null):
    global Contador
    print("Posicion reiniciada!")
    Contador = 0

GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback = deteccionGiro, bouncetime = 50)
GPIO.add_event_detect(PIN_SW, GPIO.FALLING, callback = resetContador, bouncetime = 50)
print("Prueba del modulo [Presiona Ctrl + C para finalizar la prueba]")

try:
    while True:
        time.sleep(retraso)

except KeyboardInterrupt:
    GPIO.cleanup()