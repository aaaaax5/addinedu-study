#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char *ssid = "addinedu_class_1(2.4G)";
const char *password = "addinedu1";

AsyncWebServer server(80);
void handle_root();

const char html[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
  <body>
  <center>
  <h1>Hello, ESP32 web Server!</h1>
  <a href="on"><button>LED ON</button></a>
  <a href="off"><button>LED OFF</button></a>
  </center>
  </body>
  </html>
)rawliteral";


String processor(const String& var) {
  Serial.println(var);
  return var;
}


const int ledPin = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 Web Server Start");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, [] (AsyncWebServerRequest *req) {
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/on", HTTP_GET, [] (AsyncWebServerRequest *req) {
    digitalWrite(ledPin, HIGH);
    req->send_P(200, "text/html", html, processor);
  });

server.on("/off", HTTP_GET, [] (AsyncWebServerRequest *req) {
    digitalWrite(ledPin, LOW);
    req->send_P(200, "text/html", html, processor);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);

}

void loop() {
  // put your main code here, to run repeatedly:
}
