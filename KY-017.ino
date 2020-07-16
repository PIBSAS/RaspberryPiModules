int Pin_S = 3;
int tiltVal; 
boolean bIsTilted;

void setup()
{
  Serial.begin(9600);
  pinMode(Pin_S,INPUT);
}

void loop(){
  tiltVal = digitalRead(Pin_S);
  if(tiltVal == HIGH) 
  {
    if(!bIsTilted){
      bIsTilted = true;
      Serial.println("Inclinado");
    } 
  }
  else
  {
    if(bIsTilted){
      bIsTilted = false;
      Serial.println("No inclinado");
    }    
  }
}
