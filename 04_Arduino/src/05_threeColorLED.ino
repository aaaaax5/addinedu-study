const int R_LED = 3;
const int G_LED = 5;
const int B_LED = 6;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    Serial.println("----");
    char input = Serial.read();
    Serial.println(input);

    if (input == 'b') {
      analogWrite(R_LED, 0);
      analogWrite(G_LED, 0);
      analogWrite(B_LED, 255);
      Serial.println("Blue LED is ON!");
    }

    else if (input == 'g') {
      analogWrite(R_LED, 0);
      analogWrite(G_LED, 255);
      analogWrite(B_LED, 0);
      Serial.println("Green LED is ON!");
    }

    else if (input == 'r') {
      analogWrite(R_LED, 255);
      analogWrite(G_LED, 0);
      analogWrite(B_LED, 0);
      Serial.println("Red LED is ON!");
    }

    else if (input == 'm') {
      analogWrite(R_LED, 255);
      analogWrite(G_LED, 0);
      analogWrite(B_LED, 255);
      Serial.println("Magenta is ON!");
    }

    else if (input == 'c') {
      analogWrite(R_LED, 0);
      analogWrite(G_LED, 255);
      analogWrite(B_LED, 255);
      Serial.println("Cyaan is ON!");
    }

    else if (input == 'y') {
      analogWrite(R_LED, 255);
      analogWrite(G_LED, 255);
      analogWrite(B_LED, 0);
      Serial.println("Yellow is ON!");
    }

    else {
      Serial.println("Not a command !!");
    }
  }
}
