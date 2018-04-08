
#include <SoftwareSerial.h>
SoftwareSerial sender(6, 7);
SoftwareSerial reciever(10, 11);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  reciever.begin(9600);

  delay(2000);

  sender.write("AT");
  reciever.write("AT");

  delay(2000);

  Serial.write("Sender: ");
  while (sender.available() > 0) {
    Serial.write(sender.read());
  }

  Serial.write("Reciever: ");
  while (reciever.available() > 0) {
    Serial.write(reciever.read());
  }

  Serial.println("");


  reciever.write("AT+RX");

  delay(1000);
  Serial.write("Reciever: ");
  while (reciever.available() > 0) {
    Serial.write(reciever.read());
  }




}


void loop() {


}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
