// C++ code
//
#include<Servo.h>
Servo s;
void setup()
{
  pinMode(2,INPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  s.attach(3);
  Serial.begin(9600);
}

void loop()
{
  int status = digitalRead(2);
  if(status == 1)
  {
    digitalWrite(13,HIGH);
    tone(12,250);
    delay(100);
    noTone(12);
    s.write(90);
    delay(10000);
    digitalWrite(13,LOW);
  }
  else
  {
    digitalWrite(13,LOW);
    s.write(0);
  }
}
