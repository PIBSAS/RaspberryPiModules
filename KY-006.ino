int Pin_S = 8;                                    
 
void setup()
{
  pinMode(Pin_S,OUTPUT);         
}
 
void loop()
{
  unsigned char i;
  while(1)
  { 
    //Frecuencia 1
    for(i = 0; i < 80; i++) 
    {
      digitalWrite(Pin_S,HIGH);
      delay(1);
      digitalWrite(Pin_S,LOW);
      delay(1);
    }
    //Frecuencia 2
    for(i = 0; i < 100; i++) 
    {
      digitalWrite(Pin_S,HIGH);
      delay(2);
      digitalWrite(Pin_S,LOW);
      delay(2);
    }
  }
}
