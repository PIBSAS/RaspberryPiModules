#Importamos la librería gpiozero y su función LED, además la función sleep de time
from gpiozero import LED
from time import sleep

#Declaramos ambos leds y a cuales esta conectado, lo tomamos como BCM:GPIO23 y GPIO18
rojo = LED(23)
verde = LED(18)

#Como siempre nuestro bucle
while True:
    rojo.on()
    sleep(1)
    rojo.off()
    sleep(1)
    verde.on()
    sleep(1)
    verde.off()
    sleep(1)