from Adafruit_ADS1x15 import ADS1x15
from time import sleep
import time, signal, sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

retraso = 0.5
# Asignar el ADS1x15 ADC
ADS1015 = 0x00
ADS1115 = 0x01
# Elegir la amplificación gain
gain = 4096    # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# Elegir el radio de muestreo
# sps = 8    # 8  Muestras por segundo
# sps = 16   # 16 Muestras por segundo
# sps = 32   # 32 Muestras por segundo
sps = 64     # 64 Muestras por segundo
# sps = 128  # 128 Muestras por segundo
# sps = 250  # 250 Muestras por segundo
# sps = 475  # 475 Muestras por segundo
# sps = 860  # 860 Muestras por segundo

# Asignando el canal ADC-Channel (1-4)
adc_channel_0 = 0    # Canal 0
adc_channel_1 = 1    # Canal 1
adc_channel_2 = 2    # Canal 2
adc_channel_3 = 3    # Canal 3
# Inicializa ADC (ADS1115)
adc = ADS1x15(ic=ADS1115)

try:
    while True:
        # Leemos los valores de cada ADC
        adc0 = adc.readADCSingleEnded(adc_channel_0, gain, sps)
        adc1 = adc.readADCSingleEnded(adc_channel_1, gain, sps)
        adc2 = adc.readADCSingleEnded(adc_channel_2, gain, sps)
        adc3 = adc.readADCSingleEnded(adc_channel_3, gain, sps)
        # Lo mostramos en la consola
        print("Canal 0:", adc0, "mV ")
        print("Canal 1:", adc1, "mV ")
        print("Canal 2:", adc2, "mV ")
        print("Canal 3:", adc3, "mV ")
        print("---------------------")
        time.sleep(retraso)

except KeyboardInterrupt:
    GPIO.cleanup()