int Pin_Signal = 10;       
int valor;     // Declaramos una variable temporal
  
void setup()
{
  pinMode(LED_BUILTIN,OUTPUT);         
  pinMode(Pin_Signal,INPUT);         
  digitalWrite(Pin_Signal,HIGH);       
}
  
void loop()
{
  valor = digitalRead(Pin_Signal);            
  
  if(valor == HIGH)                              
  {
    digitalWrite(LED_BUILTIN,LOW);
  }
  else
  {
    digitalWrite(LED_BUILTIN,HIGH);
  }
}
