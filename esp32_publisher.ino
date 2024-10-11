#include <PubSubClient.h>
#include <SPI.h>
#include <WiFi.h>


const char* ssid = "Livebox-1F10";
const char* password = "zPUFF5vxytpGU4xeU3";

const char* mqtt_broker = "192.168.1.19";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

const char* MQTT_TOPIC_LUM = "lum";
const char* MQTT_TOPIC_BTN = "btn";

const int photoresistorPin = 36; // Broche GPIO pour la photoresistance
const int buttonPin = 23;         // Broche GPIO pour le bouton
void setup_wifi() {
    Serial.begin(9600);
    
    delay(10);
    // Connexion au réseau WiFi
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print("Connecting to WiFi..");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    // Connexion au broker MQTT
    client.setServer(mqtt_broker, mqtt_port);

    while (!client.connected()) {
        if (client.connect("arduinoClient")) {
            Serial.println("Public MQTT broker connected");
        } else {
            delay(2000);
            Serial.print("failed with state "); 
            Serial.println(client.state());
        } 
    }
}
void setup() {
    Serial.begin(9600);
    pinMode(photoresistorPin, INPUT);
    pinMode(buttonPin, INPUT_PULLUP);

    setup_wifi();
    client.setServer(mqtt_broker, mqtt_port);
    Serial.print("broker connected "); 

}

void loop() {
  //etalonage du capteur
    client.loop();
    
    int luminosity = map(analogRead(photoresistorPin), 4095, 0, 0, 100);
    int buttonState = !digitalRead(buttonPin); 

    
    client.publish(MQTT_TOPIC_LUM, String(luminosity).c_str());
    client.publish(MQTT_TOPIC_BTN, String(buttonState).c_str());
    Serial.print("Luminosity: ");
    Serial.print(luminosity);
    Serial.print(", Button State: ");
    Serial.println(buttonState);
    delay(1000);
}
