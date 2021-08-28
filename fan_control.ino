//Initializing LED Pin
int pwm_pin = 3;
int pwm_value = 60;
int new_value;

void setup() {
  pinMode(pwm_pin, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(1);
  analogWrite(pwm_pin, pwm_value);
}

void loop() {
  while (!Serial.available());
  delay(250);
  new_value = Serial.readString().toInt();
  Serial.println(new_value);
  if (new_value >= 0 && new_value <= 255) {
    pwm_value = new_value;
    analogWrite(pwm_pin, new_value);
    }
 delay(250);
}
