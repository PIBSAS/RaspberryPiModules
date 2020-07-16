int Pin_OUT = 10;

void setup()
{
  Serial.begin(9600);
  pinMode(Pin_OUT,INPUT);
}

void loop()
{
  bool valor = digitalRead(Pin_OUT);
  if(valor == HIGH)
  {
    Serial.println("Sin obstaculos");
  }
  else
  {
    Serial.println("Obstaculo detectado");
  }
  Serial.println("---------------------");
  delay(500);
}
