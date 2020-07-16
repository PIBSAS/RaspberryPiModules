#include <Adafruit_ADS1015.h>

Adafruit_ADS1115 ads;
void setup(void)
{
  Serial.begin(9600);
  Serial.println("Valores de las entradas analogas del ADS1115 (A0..A3) seran leidas y mostradas en el monitor serie");
  Serial.println("Rango ADC: +/- 6.144V (1 bit = 0.1875mV)");
  /* El modulo incluye un amplificador de señal en las entradas, que pueden ser configuradas en la sección de abajo vía software
  Esto se busca si esperas un rango especifico de tensión como resultado de la medición,para obtener una resolución mayor de señal de amplificación es elegida por default debes marcar la activa y comentar las demás */
  ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V 1 bit = 0.1875mV
  // ads.setGain(GAIN_ONE);     // 1x gain   +/- 4.096V 1 bit = 0.125mV
  // ads.setGain(GAIN_TWO);     // 2x gain   +/- 2.048V 1 bit = 0.0625mV
  // ads.setGain(GAIN_FOUR);    // 4x gain   +/- 1.024V 1 bit = 0.03125mV
  // ads.setGain(GAIN_EIGHT);   // 8x gain   +/- 0.512V 1 bit = 0.015625mV
  // ads.setGain(GAIN_SIXTEEN); // 16x gain  +/- 0.256V 1 bit = 0.0078125mV
  ads.begin();
}

void loop(void)
{
  uint16_t adc0, adc1, adc2, adc3;
  float voltage0, voltage1, voltage2, voltage3;
  float gain_conversion_factor;
  /* El comando ads.readADC_SignalEnded(0) es la operación que comienza la medición del ADC
   *  La variable con el valor 0 define el canal medido Si queremos medir el tercer canal colocaremos 3 en lugar de cero */
   adc0 = ads.readADC_SingleEnded(0);
   adc1 = ads.readADC_SingleEnded(1);
   adc2 = ads.readADC_SingleEnded(2);
   adc3 = ads.readADC_SingleEnded(3);
   // Se necesita este valor para calcular la tensión
   gain_conversion_factor = 0.1875;
   // Calculo de los valores de tensión desde los valores medidos
   voltage0 = (adc0 * gain_conversion_factor);
   voltage1 = (adc1 * gain_conversion_factor);
   voltage2 = (adc2 * gain_conversion_factor);
   voltage3 = (adc3 * gain_conversion_factor);
   // Los valores se mostraran por el monitor serie
   Serial.print("Entrada Analoga 0: ");Serial.print(voltage0);Serial.print("mV");
   Serial.print("Entrada Analoga 1: ");Serial.print(voltage1);Serial.print("mV");
   Serial.print("Entrada Analoga 2: ");Serial.print(voltage2);Serial.print("mV");
   Serial.print("Entrada Analoga 3: ");Serial.print(voltage3);Serial.print("mV");
   Serial.println("------------------------");
   delay(1000);
}
