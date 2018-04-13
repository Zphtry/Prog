
#include <SoftwareSerial.h>
SoftwareSerial sender(8, 9);
int setPin = 7;

String command = "";


void setup() {

  Serial.begin(9600);
  sender.begin(9600);

  pinMode(setPin, OUTPUT);
  digitalWrite(setPin, HIGH);
}



void loop() {

  command = readSerial();

  if (command == "config=true") {
    enableConfig();
  }

  else

  if (command == "config=false") {
    disable_config();
  }

  else {
    sender.print(command);
  }



  Serial.print(readSender());


  delay(500);

  command = "";
}

void enableConfig() {
  digitalWrite(setPin, LOW);
}

void disable_config() {
  digitalWrite(setPin, HIGH);
}



String readSerial() {
  String command = "";

  while (Serial.available() > 0) {
    command += char(Serial.read());
  }

  return command;
}

String readSender() {
  String command = "";

  while (sender.available() > 0) {
    command += char(sender.read());
  }

  return command;
}




// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
