from machine import Pin
import utime

# Initialize passive buzzer
buzzer = Pin(2, Pin.OUT)

# Simulate two different frequencies
while True:
    # Output 500HZ frequency sound
    for i in range(80):
        buzzer.value(1)
        utime.sleep(0.001)
        buzzer.value(0)
        utime.sleep(0.001)

    # Output 250HZ frequency sound
    for i in range(100):
        buzzer.value(1)
        utime.sleep(0.002)
        buzzer.value(0)
        utime.sleep(0.002)
#End
