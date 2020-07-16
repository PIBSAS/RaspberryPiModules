int Pin_Signal = 13;

void setup()
{
  pinMode(Pin_Signal, OUTPUT);
}
void loop()
{
  digitalWrite(Pin_Signal, HIGH);
  delay(4000);
  digitalWrite(Pin_Signal, LOW);
  delay(2000);
}
