import time
import board
#import digitalio #Para usar con SPI
import busio
import adafruit_bmp280
# O creamos la variable spi para usar el puerto Bus SPI
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bmp_cs = digitalio.DigitalInOut(board.D10)
#bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# Creamos la variable i2c para utilizar el puerto Bus I2C
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
# Cambiar esto para coincidir con el lugar de la presión (hPa) a nivel del mar
bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperatura: %0.1f C" % bmp280.temperature)
    print("Presion: %0.1f hPa" % bmp280.pressure)
    print("Altitud = %0.2f metros" % bmp280.altitude)
    time.sleep(2)