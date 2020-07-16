int Pin_Signal = 10;

int retraso = 1;

void setup()
{
  pinMode(Pin_Signal,OUTPUT);
}

void loop()
{
  digitalWrite(Pin_Signal,HIGH);
  delay(retraso * 1000);
  digitalWrite(Pin_Signal,LOW);
  delay(retraso * 1000);
}
