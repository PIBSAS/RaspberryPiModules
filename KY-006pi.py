import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
GPIO_Pin_Signal = 24
GPIO.setup(GPIO_Pin_Signal,GPIO.OUT)
Frecuencia = 500    # En Hertz
pwm = GPIO.PWM(GPIO_Pin_Signal, Frecuencia)
pwm.start(50)

try:
    while True:
        print("--------------------")
        print("Frecuencia actual: %d" % Frecuencia)
        Frecuencia = input("Por favor entra una nueva frecuencia entre (50-5000):")
        pwm.ChangeFrequency(Frecuencia)
         
except KeyboardInterrupt:
    GPIO.cleanup()