from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import math, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

retraso = 0.5 
ADS1015 = 0x00
ADS1115 = 0x01
gain = 4096
sps = 64
adc_channel_0 = 0
adc_channel_1 = 1
adc_channel_2 = 2
adc_channel_3 = 3
adc = ADS1x15(ic=ADS1115)

# Funcion para calcular la temperatura a traves de la tension
def calcTemp(voltage):
    temperature = math.log((10000/voltage)*(3300-voltage))
    temperature = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temperature * temperature)) * temperature);
    temperature = temperature - 273.15;
    return temperature

try:
    while True:
        #Lee la tension y calcula la temperatura
        temp0 = round(calcTemp(adc.readADCSingleEnded(adc_channel_0,gain,sps)),2)
        temp1 = round(calcTemp(adc.readADCSingleEnded(adc_channel_1,gain,sps)),2)
        temp2 = round(calcTemp(adc.readADCSingleEnded(adc_channel_2,gain,sps)),2)
        temp3 = round(calcTemp(adc.readADCSingleEnded(adc_channel_3,gain,sps)),2)
        print("Channel 0:", temp0, "C")
        print("Channel 1:", temp1, "C")
        print("Channel 2:", temp2, "C")
        print("Channel 3:", temp3, "C")
        print("-------------------")
        sleep(retraso)
        
except KeyboardInterrupt:
    GPIO.cleanup()