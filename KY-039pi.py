from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import time, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

latidos_por_minuto = 0
isPeak = False
result = False
retraso = 0.01
maxValue = 0
schwelle = 25
beatTime = 0
oldBeatTime = 0
ADS1015 =0x00
ADS1115 = 0x01
gain = 4096
sps = 8
adc_channel = 0
adc = ADS1x15(ic=ADS1115)
LED = 24

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
def heartBeatDetect(schwelle):
    global maxValue
    global isPeak
    global result
    global oldBeatTime
    rawValue = adc.readADCSingleEnded(adc_channel, gain, sps)
    if result == True:
        result = False
        if rawValue * 4 < maxValue:
            maxValue = rawValue * 0.8;
            if rawValue > maxValue:
                maxValue = rawValue
            if isPeak == False:
                result = True
            isPeak = True
        else:
            if rawValue < maxValue - schwelle:
                isPeak = False
                maxValue = maxValue - schwelle / 2
        if result == True:
            beatTime = time.time()
            timedifference = beatTime - oldBeatTime
            latidos_por_minuto = 60 / timedifference
            oldBeatTime = beatTime
            GPIO.output(LED,GPIO.HIGH)
            time.sleep(retraso * 10)
            GPIO.output(LED,GPIO.LOW)
    return latidos_por_minuto

try:
    while True:
        time.sleep(retraso)
        latidos_por_minuto = heartBeatDetect(schwelle)
        if result == True:
            print("-Heartbeat detected !- Puls: ", int(latidos_por_minuto),"(bpm)")

except KeyboardInterrupt:
    GPIO.cleanup()