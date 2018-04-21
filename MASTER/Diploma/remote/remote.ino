
#include <SoftwareSerial.h>
// SoftwareSerial reciever(10, 11);

int setPin = 7;
SoftwareSerial sender(5, 6);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  // reciever.begin(9600);

  pinMode(setPin, OUTPUT);

  digitalWrite(setPin, LOW);

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
