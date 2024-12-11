#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper stepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  Serial.begin(9600);
  stepper.setSpeed(60);
}

void loop() {
  if (Serial.available()) {
    int steps = Serial.parseInt();
    stepper.step(steps);
  }
}
