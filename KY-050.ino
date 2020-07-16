#define Echo_Pin 7
#define Trigger_Pin 8

int rangoMax = 300; // 300 cm
int rangoMin = 2; // 2 cm
long distancia;
long duracion;
void setup()
{
  pinMode(Trigger_Pin, OUTPUT);
  pinMode(Echo_Pin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(Trigger_Pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trigger_Pin, LOW);
  duracion = pulseIn(Echo_Pin, HIGH);
  distancia = duracion / 58.2;
  if(distancia >= rangoMax || distancia <= rangoMin)
  {
    Serial.println("Fuera de rango de medición");
  }
  else
  {
    Serial.print("La distancia es de: ");
    Serial.print(distancia);
    Serial.println("cm");
    Serial.println("------------------");
  }
  delay(500);
}
