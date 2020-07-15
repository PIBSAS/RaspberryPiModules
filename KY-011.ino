int Led_Rojo = 11;
int Led_Verde = 10;

void setup()
{
  pinMode(Led_Rojo,OUTPUT);
  pinMode(Led_Verde,OUTPUT);
}

void loop()
{
  digitalWrite(Led_Rojo, HIGH);
  digitalWrite(Led_Verde, LOW);
  delay(3000);
  digitalWrite(Led_Rojo,LOW);
  digitalWrite(Led_Verde,HIGH);
  delay(3000); 
}
