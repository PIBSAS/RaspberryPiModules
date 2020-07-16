int VR_X = A0; 
int VR_Y = A1;
int SW = 7;

void setup()
{
  pinMode(VR_X,INPUT);
  pinMode(VR_Y,INPUT);
  pinMode(SW,INPUT);
  
  digitalWrite(SW,HIGH);
  
  Serial.begin(9600);
}

void loop()
{
  float x, y;
  int Boton;
  
  x = analogRead((VR_X) * (5.0 / 1023.0));
  y = analogRead((VR_Y) * (5.0 / 1023.0));
  Boton = digitalRead(SW);
  
  Serial.print("X-axis:"); Serial.print(x,4); Serial.print("V, ");
  Serial.print("Y-axis:"); Serial.print(y,4); Serial.print("V, ");
  Serial.print ("Boton:");
  if(Boton == 1)
  {
    Serial.println("no presionado");
  }
  else
  {
    Serial.println("presionado");
  }
  delay(200);
}
