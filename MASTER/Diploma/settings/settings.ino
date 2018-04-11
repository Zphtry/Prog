
#include <SoftwareSerial.h>
SoftwareSerial sender(6, 7);
// SoftwareSerial reciever(10, 11);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  pinMode(D1, INPUT_PILLDOWN);
}


void loop() {
  sender.write("test");

  delay(2000);
  Serial.write(sender.read());
}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
