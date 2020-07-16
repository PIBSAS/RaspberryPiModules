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
Digital = 24

GPIO.setup(Digital, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

try:
    while True:
        analog = adc.readADCSingleEnded(adc_channel_0, gain, sps)
        if GPIO.input(Digital) == False:
            print("Tension analoga:", analog, "mV, ", "Valor extremo: no alcanzado")
        else:
            print("Tension analoga:", analog, "mV, ", "Valor extremo: alcanzado")
            print("------------------")
            sleep(retraso)
except KeyboardInterrupt:
    GPIO.cleanup()