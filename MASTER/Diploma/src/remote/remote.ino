
#include <SoftwareSerial.h>
// SoftwareSerial reciever(10, 11);

int setPin = 2, lightPin = 5;
SoftwareSerial sender(3, 4);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  // reciever.begin(9600);

  pinMode(setPin, OUTPUT);
  pinMode(lightPin, OUTPUT);

  digitalWrite(setPin, LOW);
  digitalWrite(lightPin, HIGH);

}


void loop() {
  sender.write("AT");

  // while (Serial.available() > 0) {
  //   sender.write(Serial.read());
  // }

  // while (reciever.available() > 0) {
  //   Serial.write(reciever.read());
  // }

  delay(500);

  Serial.write(sender.read());

}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
