int Pin_Signal = 3; 
int valor;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(Pin_Signal, INPUT);
}

void loop()
{
  valor = digitalRead(Pin_Signal);
  if(valor == HIGH)
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
  else
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
}
