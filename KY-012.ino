int Pin_S = 8;

void setup()
{
  pinMode(Pin_S,OUTPUT); 
}

void loop() 
{
  digitalWrite(Pin_S,HIGH);
  delay(4000);
  digitalWrite(Pin_S,LOW);
  delay(2000); 
}
