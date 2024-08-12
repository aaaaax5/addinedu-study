const int SoundSensor = A0;
const int LED_R1 = 13;
const int LED_R2 = 12;
const int LED_Y1 = 11;
const int LED_Y2 = 10;
const int LED_G1 = 9;
const int LED_G2 = 8;
const int LED_B1 = 7;
const int LED_B2 = 6;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(SoundSensor);
  Serial.println(level);
  delay(50);
}
