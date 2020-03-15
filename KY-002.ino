//Declara la variable entera Pin_Signal y le asigna el Pin Digital 10
int Pin_Signal = 10;
int valor;  // Declara la variable entera valor
  
void setup()
{
  pinMode(LED_BUILTIN,OUTPUT);          
  pinMode(Pin_Signal,INPUT);        
  digitalWrite(Pin_Signal,HIGH);      
}
void loop()
{
  // La señal actual del sensor sera leída y asignada a valor
  valor = digitalRead(Pin_Signal);
  
  if(valor == HIGH)// Si una señal es detectada el led se encenderá
  {
    digitalWrite(LED_BUILTIN,LOW);
  }
  else
  {
    digitalWrite(LED_BUILTIN,HIGH);
  }
}
