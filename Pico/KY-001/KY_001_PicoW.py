from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin
from time import sleep, sleep_ms
 
ds_pin = machine.Pin(22)
ds_sensor = DS18X20(Onewire(ds_pin))
roms = ds_sensor.scan()
 
print('Found DS devices: ', roms)
 
while True:
    ds_sensor.convert_temp()
    sleep_ms(750)
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
    sleep(5)
#End
