int Led_Rojo = 9;
int Led_Verde = 10;
int Led_Azul = 11;
 
int valor;
 
void setup(){
  pinMode(Led_Rojo,OUTPUT); 
  pinMode(Led_Verde,OUTPUT); 
  pinMode(Led_Azul,OUTPUT); 
}
void loop(){
 
   for(valor = 255; valor > 0; valor--)
      {
       analogWrite(Led_Azul,valor);
       analogWrite(Led_Verde,255-valor);
       analogWrite(Led_Rojo,128-valor);
       delay(1);
   }
   
   for(valor = 0; valor < 255; valor++)
      {
       analogWrite(Led_Azul,valor);
       analogWrite(Led_Verde, 255-valor);
       analogWrite(Led_Rojo, 128-valor);
       delay(1);
   }
}
