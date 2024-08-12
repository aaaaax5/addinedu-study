int max = 800;
int min = 600;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(A0);
  delay(500);
  Serial.println(light);
  if (max < light)
  {
    max = light;
    Serial.print('max:');
    Serial.println(max);
  }
  if (min > light)
  {
    min = light;
    Serial.print(', min:');
    Serial.println(min);
  }
}
