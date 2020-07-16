int Led_Rojo = 9;
int Led_Verde = 10;
int Led_Azul = 11;
void setup()
{
  pinMode(Led_Rojo, OUTPUT);
  pinMode(Led_Verde, OUTPUT);
  pinMode(Led_Azul, OUTPUT);
}
void loop(){
  digitalWrite(Led_Rojo, HIGH);
  digitalWrite(Led_Verde, LOW);
  digitalWrite(Led_Azul, LOW);
  delay(3000);
  
  digitalWrite(Led_Rojo, LOW);
  digitalWrite(Led_Verde, HIGH);
  digitalWrite(Led_Azul, LOW);
  delay(3000);
  
  digitalWrite(Led_Rojo, LOW);
  digitalWrite(Led_Verde, LOW);
  digitalWrite(Led_Azul, HIGH);
  delay(3000);
}
