#!/usr/bin/env python3
# coding=utf-8
# Importamos los modulos necesarios
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
# configuramos una pausa de 2 segundos
sleeptime = 2
# El sensor debe ser configurado como Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, o Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
# Declaramos a que  lo hemos conectado
GPIO_Pin_Signal = 23
print("KY-015 prueba de Temperatura y humedad")
try:
    while(1):
        # La medicion sera escrita en las variables humid temper
        humedad,temperatura = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin_Signal)
        print("-------")
        if humedad is not None and temperatura is not None:
            # El resultado se muestra en consola
            print("Temperatura = {0:0.1f}°C | rel. humidity = {1:0.1f}%’.format(temperatura, humedad)")
        # A causa del sistema Linux, la Raspberry Pi tiene problemas para obtener
        # mediciones en tiempo real.
        # Esto es por, problemas de sincronización, lo que causa fallas de
        # comunicación.
        # En ese caso, un mensaje de error se mostrará – el resultado se mostrará   
        # en el próximo intento.
        else:
            print("Error al leer, por favor reintentalo!")
            print("-------")
            print(" ")
            time.sleep(sleeptime)
# Limpiamos los estados de GPIO
except KeyboardInterrupt:
    GPIO.cleanup()
