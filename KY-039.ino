//Al compilar mantener el Pin_S desconectado del Pin 0 de Arduino o dará fallo
int Pin_S = 0;
const int muestreo = 60;
int valor;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Latidos");
}

void loop()
{
  static int latido_por_segundos = 0;
  int pulsobpm = 0;
  
  Serial.println(valor);
  if(deteccion(Pin_S, muestreo))
  {
    pulsobpm = 60000 / latido_por_segundos;
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.print(valor);
    Serial.print(",");
    Serial.println(pulsobpm);
    latido_por_segundos = 0;
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(muestreo);
  latido_por_segundos = latido_por_segundos + muestreo;
}

bool deteccion(int IrSensor, int retardo)
{
  static int maximo = 0;
  static bool pico = false;
  bool resultado = false;
  valor = analogRead(IrSensor);
  valor = valor * (1000/retardo);
  if(valor * 4L < maximo)
  {
    maximo = valor * 0.8;
    if(valor > maximo)
    {
      maximo = valor;
    }
    if(pico == false)
    {
      resultado = true;
    }
    pico = true;
  }
  else if(valor < maximo - (3000 / retardo))
  {
    pico = false;
    maximo = maximo - (1000 / retardo);
  }
  return resultado;
}
