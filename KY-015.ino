// Incluímos la librería Adafruit_DHT
#include <DHT_U.h>
#include <DHT.h>

// Declaramos el pin de entrada
#define DHTPIN 8

// Inicializamos el sensor
#define DHTTYPE DHT11 //DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup(){
  Serial.begin(9600);
  Serial.println("Prueba KY-015: ");
  // Comenzamos la medición
  dht.begin();
}

void loop()
{
  // Pausa de 2 segundos entre medición
  delay(2000);
  // Medición de humedad
  float h = dht.readHumidity();
  // Medición de temperatura
  float t = dht.readTemperature();
  // Se probarán errores de mediciones
  
  // Si un error es detectado se muestra un mensaje de error
  if(isnan(h)||isnan(t))
  {
    Serial.println("Error mientras leía el sensor");
    return;
  }
  // Salida por Monitor Serie
  Serial.println("-----------");
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(char(186)); // Salida <°> simbolo grado
  Serial.println("C ");
  Serial.println("-----------");
  Serial.println(" ");
}
