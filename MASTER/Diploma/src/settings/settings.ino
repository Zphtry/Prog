
#include <SoftwareSerial.h>
//                 TXD RXD
SoftwareSerial radio(6, 7);
int setPin = 5;

String command = "";


void setup() {

  Serial.begin(9600);
  radio.begin(9600);

  pinMode(setPin, OUTPUT);
  digitalWrite(setPin, HIGH);

  getConfigStatus();
}



void loop() {

  command = readSerial();

  if (command.length() > 0) {
    if (command == "config.enable") {
      enableConfig();
    }

    else if (command == "config.disable") {
      disableConfig();
    }

    else if (command == "config.status") {
      getConfigStatus();
    }

    else {
      radio.print(command);
      Serial.println("MESSAGE: " + command);
    }
  }

  readRadio();

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

void getConfigStatus() {
  if (digitalRead(setPin) == 0) {
    Serial.println("CONFIG=TRUE");
  } else {
    Serial.println("CONFIG=FALSE");
  }
}



String readSerial() {
  String command = "";

  while (Serial.available() > 0) {
    command += char(Serial.read());
  }

  return command;
}

String readRadio() {
  String response = "";

  while (radio.available() > 0) {
    response += char(radio.read());
  }

  if (response.length() > 0) {
    response = "RESPONSE: " + response;
    Serial.print(response);
    return response;
  }

}




// прерывания
// процессор (datasheet)
// http://www.airspayce.com/mikem/arduino/RadioHead/
// разобраться в настройках (особенно дистанционное управ)
