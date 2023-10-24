from machine import ADC, Pin

# setup the Pulse Sensor reading pin
pulse=ADC(26)
led = Pin(25, Pin.OUT)

max_samples = 1000
short_average=15
long_average=100
beat_threshold=200
finger_threshold=2000
history = []


def finger_detected():
    avg_1=sum(history[-short_average:])/short_average
    avg_2=sum(history[-long_average:])/long_average
    if avg_1-avg_2 > beat_threshold:
        led.value(1)
    else:
        led.value(0)

# main program
while True:
    try:
        value=pulse.read_u16()
        history.append(value)
        history = history[-max_samples:]
        
        if max(history)-min(history) < finger_threshold:
            finger_detected()
        else:
            led.value(0)
            
    except OSError as e:
        machine.reset()
#End
