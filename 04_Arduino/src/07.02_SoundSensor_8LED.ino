const int SoundSensor = A0;
const int LED_R1 = 13;
const int LED_R2 = 12;
const int LED_Y1 = 11;
const int LED_Y2 = 10;
const int LED_G1 = 9;
const int LED_G2 = 8;
const int LED_B1 = 7;
const int LED_B2 = 6;

int minSound = 250;
int maxSound = 500;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(SoundSensor);
  level = level * 2;
  // Serial.println(level);
  delay(50);

  if (minSound > level) 
  {
    minSound = level;
    Serial.print("minSound: ");
    Serial.println(minSound);
  }
  else if (maxSound < level)
  {
    maxSound = level;
    Serial.print("maxSound: ");
    Serial.println(maxSound);    
  }

  if (level <= 110) 
  {
    level = 110;
  }
  else if (level >= 1780)
  {
    level = 1780;
  }

  if (level >= 110 && level < 318)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, LOW);
    digitalWrite(LED_Y2, LOW);
    digitalWrite(LED_G1, LOW);
    digitalWrite(LED_G2, LOW);
    digitalWrite(LED_B1, LOW);
    digitalWrite(LED_B2, HIGH);
  }
  else if (level >= 318 && level < 527)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, LOW);
    digitalWrite(LED_Y2, LOW);
    digitalWrite(LED_G1, LOW);
    digitalWrite(LED_G2, LOW);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
  else if (level >= 527 && level < 736)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, LOW);
    digitalWrite(LED_Y2, LOW);
    digitalWrite(LED_G1, LOW);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
  else if (level >= 736 && level < 945)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, LOW);
    digitalWrite(LED_Y2, LOW);
    digitalWrite(LED_G1, HIGH);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
  else if (level >= 945 && level < 1153)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, LOW);
    digitalWrite(LED_Y2, HIGH);
    digitalWrite(LED_G1, HIGH);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
    else if (level >= 1153 && level < 1362)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, LOW);    
    digitalWrite(LED_Y1, HIGH);
    digitalWrite(LED_Y2, HIGH);
    digitalWrite(LED_G1, HIGH);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
    else if (level >= 1362 && level < 1571)
  {
    digitalWrite(LED_R1, LOW);
    digitalWrite(LED_R2, HIGH);    
    digitalWrite(LED_Y1, HIGH);
    digitalWrite(LED_Y2, HIGH);
    digitalWrite(LED_G1, HIGH);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }
    else
  {
    digitalWrite(LED_R1, HIGH);
    digitalWrite(LED_R2, HIGH);    
    digitalWrite(LED_Y1, HIGH);
    digitalWrite(LED_Y2, HIGH);
    digitalWrite(LED_G1, HIGH);
    digitalWrite(LED_G2, HIGH);
    digitalWrite(LED_B1, HIGH);
    digitalWrite(LED_B2, HIGH);
  }      
}