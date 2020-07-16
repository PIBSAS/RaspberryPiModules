#include <IRremote.h>
#include <IRremoteInt.h>

int Pin_Signal = 11;

IRrecv irrecv(Pin_Signal);
decode_results resultado;
  
void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
  }
  
void loop() {
  if (irrecv.decode(&resultado)) {
    Serial.println(resultado.value, HEX);
    irrecv.resume(); 
  }
}
