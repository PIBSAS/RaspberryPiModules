from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import time, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

retraso = 0.5
ADS1115 = 0x01
gain = 4096
sps = 64
adc_channel_0 = 0
adc_channel_1 = 1
adc_channel_2 = 2
adc_channel_3 = 3
adc = ADS1x15(ic=ADS1115)

try:
    while True:
        adc0 = adc.readADCSingleEnded(adc_channel_0, gain, sps)
        adc1 = adc.readADCSingleEnded(adc_channel_1, gain, sps)
        adc2 = adc.readADCSingleEnded(adc_channel_2, gain, sps)
        adc3 = adc.readADCSingleEnded(adc_channel_3, gain, sps)
        print("Channel 0: ", adc0, "mV ")
        print("Channel 1: ", adc1, "mV ")
        print("Channel 2: ", adc2, "mV ")
        print("Channel 3: ", adc3, "mV ")
        time.sleep(retraso)

except KeyboardInterrupt:
    GPIO.cleanup()