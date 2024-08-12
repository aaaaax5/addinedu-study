#include <Servo.h>
Servo servo;
int sensorPin = A0;
int sensorValue = 0;
int val;
void setup() {
  servo.attach(9);
  Serial.begin(9600);
  servo.write(30);
}
void loop() {
  sensorValue = (analogRead(sensorPin));
  if (sensorValue < 40) {
    val = 50; 
    servo.write(val);
    delay(285);
  }
  else {
    val =  0;
    servo.write(val);
    delay(10);
  }
  Serial.println(sensorValue);
} 