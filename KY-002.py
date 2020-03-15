#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  KY-002.py
#  
#  Copyright 2020  <lucianorabassa@gmail.com>
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Se declara el Pin de entrada del sensor y se activa la resistencia pull-up.
GPIO_Pin_Signal = 24
GPIO.setup(GPIO_Pin_Signal, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("Probar Sensor [presiona ctrl+c para terminar la prueba]")

# Esta función será llamada al detectarse el sensor
def funcionDetectar(null):
    print("Ha sido detectada")
    
#Al momento de detectar una señal se llamará a la función funcionDetectar y se la activará
GPIO.add_event_detect(GPIO_Pin_Signal, GPIO.FALLING, callback = funcionDetectar, bouncetime = 100)

#bucle
try:
    while True:
        time.sleep(1)

# Se limpian los GPIO luego de terminado el programa
except KeyboardInterrupt:
    GPIO.cleanup()
