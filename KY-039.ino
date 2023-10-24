int rawValue;
bool heartbeatDetected(int IRSensorPin, int delay)
{
  static int maxValue = 0;
  static bool isPeak = false;
  bool result = false;
      
  rawValue = analogRead(IRSensorPin);
  // Here the current voltage value at the photo transistor is read out and stored temporarily in the rawValue variable
  rawValue *= (1000 / delay);
  
  // Should the current value deviate too far from the last maximum value
  // (e.g. because the finger was put on again or taken away)
  // So the MaxValue is reset to get a new base.
  if(rawValue * 4L <maxValue)
  {
    maxValue = rawValue * 0.8;
  } // Detect new peak
  
  if(rawValue > maxValue - (1000 / delay))
  {
    // The actual peak is detected here. Should a new RawValue be bigger
    // as the last maximum value, it will be recognized as the top of the recorded data.
    if(rawValue > maxValue)
    {
      maxValue = rawValue;
    }
    // Only one heartbeat should be assigned to the recognized peak
    if(isPeak == false)
    {
      result = true;
    }
    isPeak = true;
  }else if(rawValue < maxValue - (3000 / delay))
  {
    isPeak = false;
    // This is the maximum value for each pass
    // slightly reduced again. The reason for this is that
    // not only the value is otherwise always stable with every stroke
    // would be the same or smaller, but also,
    // if the finger should move minimally and thus
    // the signal would generally become weaker.
    maxValue -= (1000 / delay);
 }
  return result;
}
  
///////////////////////////////
// Arduino main code         //
///////////////////////////////
int ledPin = 13;
int analogPin = A0;
  
void setup()
{
  // The built-in Arduino LED (Digital 13) is used here for output
  pinMode(ledPin, OUTPUT);
  // Serial output initialization
  Serial.begin(9600);
  Serial.println("Heartbeat detection sample code.");
}
  
const int delayMsec = 60; // 100msec per sample
  
// The main program has two tasks:
// - If a heartbeat is recognized, the LED flashes briefly
// - The pulse is calculated and output on the serial output.
  
void loop()
{
  static int beatMsec = 0;
  int heartRateBPM = 0;
  if(heartbeatDetected(analogPin, delayMsec))
  {
    heartRateBPM = 60000 / beatMsec;
    // LED output at heartbeat
    digitalWrite(ledPin, 1);
  
    // Serial data output
    Serial.print("Pulse detected:");
    Serial.println(heartRateBPM);
      
    beatMsec = 0;
    
  }else
  {
    digitalWrite(ledPin, 0);
  }
  delay(delayMsec);
  beatMsec += delayMsec;
}
//End
