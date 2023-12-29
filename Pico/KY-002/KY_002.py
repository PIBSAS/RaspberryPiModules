from machine import Pin

led = Pin(25, Pin.OUT)
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
#End
