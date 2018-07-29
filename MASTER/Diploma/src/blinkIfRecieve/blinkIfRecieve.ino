
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

  digitalWrite(setPin, HIGH);
//  digitalWrite(lightPin, HIGH);

}

 
void loop() {
  sender.write("t");
  shortBlink();
//
   while (Serial.available() > 0) {
     sender.write(Serial.read());
     shortBlink();
   }

   while (sender.available() > 0) {
     Serial.write(sender.read());
     shortBlink();
   }

  delay(1000);
}

void shortBlink() {
  digitalWrite(lightPin, HIGH);
  delay(50);
  digitalWrite(lightPin, LOW);
}



// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
