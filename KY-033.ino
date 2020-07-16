int Pin_S = 3;

void setup()
{
  Serial.begin(9600);
  pinMode(Pin_S,INPUT);
}

void loop()
{
  bool valor = digitalRead(Pin_S);
  if(valor == HIGH)
  {
    Serial.println("Esta en la linea");
  }
  else
  {
    Serial.println("No esta en la linea");
  }
  delay(500);
}
