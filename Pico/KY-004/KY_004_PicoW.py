from machine import Pin
from utime import sleep
# Initialize the LED lights and buttons
led = Pin("LED", Pin.OUT)
key = Pin(28, Pin.IN, Pin.PULL_UP)
# Open the LED light that comes with the Pico board
def led_on():
    led.value(1)
    
# Close the LED light that comes with the Pico board
def led_off():
    led.value(0)
    # Read the state of the button, press to return to True, release to return to False

def press_state():
    if key.value() == 0:
        return True
    return False

# Main loop, when the button is pressed, the LED is on, and “press” is printed every 100 milliseconds;
# when the button is released, the LED is off
while True:
    if press_state() == True:
        print("press")
        led_on()
        sleep(.1)
    else:
        led_off()
#End
