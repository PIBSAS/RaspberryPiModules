from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)
sensor = Pin(22, Pin.IN)

while True:
    if sensor.value() == 1:
        led.on()
        print("ON")
        print(sensor.value())
    else:
        led.off()
        print("OFF")
        print(sensor.value())
    sleep(1)
#End