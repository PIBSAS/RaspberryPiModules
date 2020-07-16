int Contador = 0; 
boolean direccion;
int Pin_clk_anterior;  
int Pin_clk_actual;
int pin_clk = 3;  
int pin_dt = 4; 
int Pin_SW = 5;

void setup()
{
  pinMode(pin_clk, INPUT);
  pinMode(pin_dt, INPUT);
  pinMode(Pin_SW, INPUT);
  
  digitalWrite(pin_clk, true);
  digitalWrite(pin_dt, true);
  digitalWrite(Pin_SW, true);
  
  Pin_clk_anterior = digitalRead(pin_clk);
  Serial.begin(115200);
}

void loop()
{
  Pin_clk_actual = digitalRead(pin_clk);
  if(Pin_clk_actual != Pin_clk_anterior)
  {
    if(digitalRead(pin_dt) != Pin_clk_actual)
    {
      Contador++;
      direccion = true;
    }
    else
    {
      direccion = false;
      Contador--;
    }
    Serial.println("Rotacion detectada: ");
    Serial.print("Direccion de giro: ");
    if (direccion)
    {
      Serial.println("Sentido horario");
    }
    else
    {
      Serial.println("Sentido antihorario");
    }
    Serial.print("Posicion actual: ");
    Serial.println(Contador);
    Serial.println("---------------");
  }
  Pin_clk_anterior = Pin_clk_actual;
  if(!digitalRead(Pin_SW) && Contador != 0)
  {
    Contador = 0;
    Serial.println("Posicion reiniciada");
  }
}
