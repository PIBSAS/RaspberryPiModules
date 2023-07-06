#Requiere libraries micropython_ir y micropython-async
#https://sites.google.com/view/raspberrypibuenosaires/sensores-arduino-y-raspberry-pi/sensores-arduino-y-raspberry-pi-5
from machine import Pin
from ir_tx.nec import NEC
import time

nec = NEC(Pin(17, Pin.OUT, value = 0))

while True:
    nec.transmit(1, 2)  # address == 1, data == 2
    time.sleep(2)
#End
