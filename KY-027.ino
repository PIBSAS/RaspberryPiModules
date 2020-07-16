int Pin_L = 9;
int Pin_S = 8;
int valor;

void setup()
{
  pinMode(Pin_L, OUTPUT);
  pinMode(Pin_S, INPUT);
  digitalWrite(Pin_S, HIGH);
}

void loop()
{
  valor = digitalRead(Pin_S);
  if(valor == HIGH)
  {
    digitalWrite(Pin_L, LOW);
  }
  else
  {
    digitalWrite(Pin_L, HIGH);
  }
}
