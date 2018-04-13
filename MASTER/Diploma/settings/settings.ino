
#include <SoftwareSerial.h>
SoftwareSerial sender(8, 9);


void setup() {
  Serial.begin(9600);
  sender.begin(9600);
  pinMode(7, OUTPUT); 
//  reciever.begin(9600);

}


void loop() {
    digitalWrite(7, HIGH);
  
    sender.write("AT");

    while (sender.available() > 0) {
      Serial.write(sender.read());
    }

  delay(500);

}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
