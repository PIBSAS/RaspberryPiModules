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
Pin_SW = 24

GPIO.setup(Pin_SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        x = adc.readADCSingleEnded(adc_channel_0, gain, sps)
        y = adc.readADCSingleEnded(adc_channel_1, gain, sps)
        if GPIO.input(Pin_SW) == True:
            print("X-axis: ", x, "mV, ", "Y-axis: ", y, "mV, Pin_SW: no presionado")
        else:
            print("X-axis: ", x, "mV, ", "Y-axis: ", y, "mV, Pin_SW: presionado")
            print("-----------------")
            button_pressed = False
            time.sleep(retraso)

except KeyboardInterrupt:
    GPIO.cleanup()