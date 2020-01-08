# coding=utf-8
# Importamos los módulos necesarios
import glob
import time
from time import sleep
import RPi.GPIO as GPIO
 
# tiempo entre mediciones
sleeptime = 1
 
# Habilitamos la resistencia Pull UP
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# Luego de habilitada la resistencia Pull UP debemos esperar que inicie el sensor
print("aguarda que inicie el sensor...")
 
base_dir = '/sys/bus/w1/devices/'
while True:
    try:
        device_folder = glob.glob(base_dir + '28*')[0]
        break
    except IndexError:
        sleep(0.5)
        continue
device_file = device_folder + '/w1_slave'
 
# Definimos la función de medición de temperatura.
def Medición():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
Medición()
 
def EvaluarMedicion():
    lines = Medición()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = Medición()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
 
# loop
try:
    while True:
        print("---------------------------------------")
        print("Temperatura:", EvaluarMedicion(), "°C")
        time.sleep(sleeptime)
 
except KeyboardInterrupt:
    GPIO.cleanup()
