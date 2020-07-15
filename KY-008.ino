int laser = 13;

void setup()
{
 pinMode(laser,OUTPUT);                    
}

void loop(){
 digitalWrite(laser,HIGH);                   
 delay(1000);                                            
 digitalWrite(laser,LOW);                     
 delay(1000);                                            
}
