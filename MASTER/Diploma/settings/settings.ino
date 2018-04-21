
#include <SoftwareSerial.h>
SoftwareSerial sender(6, 5);
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

  if (command.length() > 0) {
    if (command == "config=true") {
      enableConfig();
    }

    else

    if (command == "config=false") {
      disableConfig();
    }

    else {
      sender.print(command);
      Serial.println("На модуль отправлено: " + command);
    }
  }



  Serial.print(readSender());
  Serial.print(sender.read());

  delay(500);

  command = "";
}

void enableConfig() {
  digitalWrite(setPin, LOW);
  Serial.println("Config enabled");
}

void disableConfig() {
  digitalWrite(setPin, HIGH);
  Serial.println("Config disabled");
}



String readSerial() {
  String command = "";

  while (Serial.available() > 0) {
    command += char(Serial.read());
  }

  return command;
}

String readSender() {
  String info = "";

  while (sender.available() > 0) {
    info += char(sender.read());
  }

  return info;
}




// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
