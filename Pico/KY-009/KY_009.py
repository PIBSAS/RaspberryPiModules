from machine import Pin
import utime
# Initialize the LED lights
red = Pin(2, Pin.OUT)
green = Pin(3, Pin.OUT)
blue = Pin(4, Pin.OUT)
# Control the red light, state=0 light is off,state= other values light is on
def rgb_red(state):
    if state == 0:
        red.value(0)
    else:
        red.value(1)

# Control the green light, state=0 light is off,state= other values light is on
def rgb_green(state):
    if state == 0:
        green.value(0)
    else:
        green.value(1)

# Control the blue light, state=0 light is off, state= other values light is on
def rgb_blue(state):
    if state == 0:
        blue.value(0)
    else:
        blue.value(1)

# Close RGB light
def rgb_off():
    red.value(0)
    green.value(0)
    blue.value(0)

# RGB light become white
def rgb_on():
    red.value(1)
    green.value(1)
    blue.value(1)

#Main loop, switch a color every 0.5s
while True:
    rgb_off()
    rgb_red(1)
    utime.sleep(.5)
    rgb_off()
    rgb_green(1)
    utime.sleep(.5)
    rgb_off()
    rgb_blue(1)
    utime.sleep(.5)
    rgb_on()
    utime.sleep(.5)
#End
