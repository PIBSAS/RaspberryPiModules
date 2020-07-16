int Pin_A0 = 0;
int Pin_D0 = 3;

void setup()
{
  pinMode(Pin_A0, INPUT);
  pinMode(Pin_D0, INPUT);
  Serial.begin(9600);
}

void loop()
{
  float Analog;
  int Digital;
  Analog = analogRead(Pin_A0) * (5.0 / 1023.0);
  Digital = digitalRead(Pin_D0);
  
  Serial.print("Tension analoga:");Serial.print(Analog,4);Serial.print("V, ");
  Serial.print("Valor extremo:");
  if(Digital == 1)
  {
    Serial.println(" alcanzado");
  }
  else
  {
    Serial.println(" no alcanzado");
  }
  Serial.println("-----------------");
  delay(200);
}
