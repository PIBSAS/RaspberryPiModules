int Pin_Signal = A3;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int valorBruto = analogRead(Pin_Signal);
  float Tension = valorBruto * (5.0/1023.0) * 1000;
  float Resistencia = 10000 * ( Tension / ( 5000.0 - Tension));
  
  Serial.print("Tension:");Serial.print(Tension);Serial.print("mV");
  Serial.print(", Resistencia:");Serial.print(Resistencia);Serial.print("Ohm");
  Serial.println("------------");
  delay(500);
}
