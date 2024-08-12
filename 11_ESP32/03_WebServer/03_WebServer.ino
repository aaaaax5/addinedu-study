#include <WiFi.h>
#include <WebServer.h>
#include <ESPAsynsncWebServer.h>

const char *ssid = "addinedu_class1_2.4G";
const char *password = "addinedu1";

WebServer server(80);
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


void handle_root() {
  server.send(200, "text/html", html);
}


void setup() {
  // put your setup code here, to run once:
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

  server.on("/", handle_root);
  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();
}
