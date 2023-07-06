from machine import Pin
from ir_tx.nec import NEC
import time

nec = NEC(Pin(17, Pin.OUT, value = 0))

while True:
    nec.transmit(1, 2)  # address == 1, data == 2
    time.sleep(2)
#End
