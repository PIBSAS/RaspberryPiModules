#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11 
#define BMP_CS 10

Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO, BMP_SCK);

void setup()
{
  Serial.begin(9600);
  if(!bmp.begin())
  {
    Serial.println(F("No se encuentra al sensor BMP280, verifica el conexionado!"));
    while (1);
  }
}

void loop()
{
  Serial.print(F("Temperatura = "));
  Serial.print(bmp.readTemperature());
  Serial.println(" *C");
  Serial.print(F("Presion = "));
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");
  Serial.println();
  delay(2000);
}
