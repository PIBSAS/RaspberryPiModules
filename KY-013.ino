#include <math.h> //Incluimos math para realizar las cuentas matematicas
int Pin_S = A0;

double Thermistor(int RawADC){
  double Temp;Temp = log(10000.0 * ((1024.0 / RawADC - 1)));
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp )) * Temp );
  Temp = Temp - 273.15;
  // conversion de grados Kelvin a Celsius
  return Temp;
  }
void setup(){
  Serial.begin(9600);
  }
void loop()
{
  int readVal = analogRead(Pin_S);
  double temp = Thermistor(readVal);
  Serial.print("La temperatura es: ");
  Serial.print(temp);
  Serial.print(char(186)); //Muestra el simbolo <°>
  Serial.println("C");
  Serial.println("---------------");
  delay(500);
}
