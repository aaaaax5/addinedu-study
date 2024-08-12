#include <Servo.h>
int pos = 0;
int speed = 1;
Servo servo;
int SERVO_PIN = 9;
const int acceleration = 4;
const int deceleration = 2;


void setup() {
  servo.attach(SERVO_PIN);
}

void loop() {
  for (pos = 10; pos <= 180; pos += speed) {
    servo.write(pos);
    delay(15);
  }
  for (pos = 180; pos >= 10; pos -= speed) {
    servo.write(pos);
    delay(15);
  }
}