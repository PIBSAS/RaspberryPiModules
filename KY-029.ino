int rojo = 10;
int verde = 11;

void setup()
{
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
}

void loop()
{
  digitalWrite(rojo, HIGH);
  digitalWrite(verde, LOW);
  delay(3000);
  
  digitalWrite(rojo, LOW);
  digitalWrite(verde, HIGH);
  delay(3000);
}
