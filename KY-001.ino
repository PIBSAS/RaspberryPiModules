#include <OneWire.h>
 
// DS18S20 Temperatura chip i/o
OneWire ds(2);  // Inicializamos el Pin 2
 
void setup(void) {

  // Inicializamos el puerto serie en 9600 baudios
  Serial.begin(9600);

}
 
void loop(void) {
 
  // Creamos las variables para convertir a grados centigrados
  int HighByte, LowByte, TReading, SignBit, Tc_100, Whole, Fract;
 
  byte i;
  byte present = 0;
  byte data[12];
  byte addr[8];
 
  if ( !ds.search(addr)) {
      Serial.print("Sin mas direcciones.\n");
      ds.reset_search();
      return;
  }
 
  Serial.print("R=");
  for( i = 0; i < 8; i++) {
    Serial.print(addr[i], HEX);
    Serial.print(" ");
  }
 
  if ( OneWire::crc8( addr, 7) != addr[7]) {
      Serial.print("CRC invalido!\n");
      return;
  }
 
  if ( addr[0] == 0x10) {
    Serial.print(" Es un dispositivo de la familia DS18S20.\n");
  }
  else if ( addr[0] == 0x28) {
      Serial.print("Es un dispositivo de la familia DS18S20 .\n");
  }
  else {
      Serial.print("Dispositivo desconocido: 0x");
      Serial.println(addr[0],HEX);
      return;
  }
 
  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);         // Comienza la conversión
 
  delay(1000); 
 
  present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);         
 
  Serial.print("P=");
  Serial.print(present,HEX);
  Serial.print(" ");
  for ( i = 0; i < 9; i++) {           // Necesitamos leer 9 bytes
    data[i] = ds.read();
    Serial.print(data[i], HEX);
    Serial.print(" ");
  }
  Serial.print(" CRC=");
  Serial.print( OneWire::crc8( data, 8), HEX);
  Serial.println();
 
  //Conversión de datos a grados centigrados
  LowByte = data[0];
  HighByte = data[1];
  TReading = (HighByte << 8) + LowByte;
  SignBit = TReading & 0x8000;  
  if (SignBit)
  {
    TReading = (TReading ^ 0xffff) + 1; 
  }
  Tc_100 = (6 * TReading) + TReading / 4;
  Whole = Tc_100 / 100; 
  Fract = Tc_100 % 100;
 
 
  if (SignBit) 
  {
     Serial.print("-");
  }
  Serial.print(Whole);
  Serial.print(".");
  if (Fract < 10)
  {
     Serial.print("0");
  }
  Serial.print(Fract);
 
  Serial.print("\n"); 
}
