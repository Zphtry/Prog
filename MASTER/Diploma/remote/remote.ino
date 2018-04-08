
#include <SoftwareSerial.h>
SoftwareSerial sender(6, 7);
SoftwareSerial reciever(10, 11);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  reciever.begin(9600);

}


void loop() {

  while (Serial.available() > 0) {
    sender.write(Serial.read());
  }

  while (reciever.available() > 0) {
    Serial.write(reciever.read());
  }

  delay(500);

}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
