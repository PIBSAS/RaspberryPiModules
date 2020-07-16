import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

Trigger_Pin = 17
Echo_Pin = 27
sleeptime = 0.8

GPIO.setup(Trigger_Pin, GPIO.OUT)
GPIO.setup(Echo_Pin, GPIO.IN)
GPIO.output(Trigger_Pin, False)

try:
    while True:
        GPIO.output(Trigger_Pin, True)
        time.sleep(0.00001)
        GPIO.output(Trigger_Pin, False)
        pulso_inicio = time.time()
        while GPIO.input(Echo_Pin) == 0:
            pulso_inicio = time.time()
        while GPIO.input(Echo_Pin) == 1:
            pulso_fin = time.time()
        duracion = pulso_fin - pulso_inicio
        distancia = (duracion * 34300) / 2
        if distancia < 2 or (round(distancia) > 300):
            print("Distancia fuera de rango")
            print("----------------")
        else:
            distancia = format((duracion * 34300) / 2, '.2f')
            print(("La distancia es de:"), distancia,("cm"))
            print("----------------")
        time.sleep(sleeptime)

except KeyboardInterrupt:
    GPIO.cleanup()