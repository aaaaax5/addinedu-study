#define TCRT5000_SENSOR_PIN 15

void setup() 
{
  Serial.begin(115200);
  pinMode(TCRT5000_SENSOR_PIN, INPUT);
}

void loop() 
{
  Serial.println(analogRead(TCRT5000_SENSOR_PIN));
  delay(100);
}