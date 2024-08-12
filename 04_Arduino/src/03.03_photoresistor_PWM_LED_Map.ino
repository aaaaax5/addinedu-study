const int LED = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(A0);

  int out = map(light, 450, 900, 255, 0);

  if (out < 5) {
    out = 5;
  }

  if (out > 250) {
    out =250;
  }
  Serial.print(light);
  Serial.print(", ");
  Serial.println(out);

  analogWrite(LED, out);
}
