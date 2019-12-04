/*
 *  TechAhoy - Ambient Computing: Weather
 *
 *  Adafruit HUZZAH32 pulling weather forecasts from OpenWeather.
 *  https://openweathermap.org/
 *
 *
 *  config.h - Private parameters
 */
 
#include "config.h"
#include <ArduinoJson.h>  
#include "WiFi.h"
#include "time.h"
 
const char* wifi = WIFI;
const char* pass =  PASS;

/* 
 *  OpenWeather Parameters
 *  Example URI: http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111
 *  City IDs: https://openweathermap.org/current#cityid
 *  
 */
String CityID = MYCITY;
String APIKEY = OWAPI;
int weatherID = 0;

// NTPTime
const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = -18000; //EST
const int   daylightOffset_sec = 3600;

WiFiClient client;
char* servername ="api.openweathermap.org";  // remote server we will connect to
String result;
int  iterations = 1800;
String weatherDescription ="";
String weatherLocation = "";
float Temperature;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(115200);
 
  enableWifi();

  //init and get the time
  //configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  //printLocalTime();
 
}
 
void loop(){
  delay(2000);
  if(iterations == 1800)//We check for updated weather forecast once every hour
   {
     getWeatherData();
     // printWeatherIcon(weatherID);
     iterations = 0;   
   }

  iterations++;
  
  blinkLED();
}

void enableWifi()
{  
  WiFi.begin(wifi, pass);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
}

void blinkLED()
{
  digitalWrite(LED_BUILTIN,HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN,LOW);
}

void printLocalTime()
{
  time_t now;
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  time(&now);
  Serial.print("time: ");
  Serial.println(now);
  Serial.println(&timeinfo);
  Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
}

void getWeatherData() //client function to send/receive GET request data.
{
  String result ="";
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(servername, httpPort)) {
        return;
    }
      // We now create a URI for the request
    String url = "/data/2.5/forecast?id="+CityID+"&units=imperial&APPID="+APIKEY;

       // This will send the request to the server
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                 "Host: " + servername + "\r\n" +
                 "Connection: close\r\n\r\n");
    unsigned long timeout = millis();
    while (client.available() == 0) {
        if (millis() - timeout > 5000) {
            client.stop();
            return;
        }
    }
    
    // Read all the lines of the reply from server
    while(client.available()) {
        result = client.readStringUntil('\r');
    }
    
  //result.replace('[', ' ');
  //result.replace(']', ' ');
  if (result.length()+1 > 1000){
    
  }
  //char jsonArray [result.length()+1];
  
  //result.toCharArray(jsonArray,sizeof(jsonArray));
  //jsonArray[result.length() + 1] = '\0';
  
  
  DynamicJsonDocument doc(25000);
  DeserializationError error = deserializeJson(doc, result);
  if (error)
  {
    Serial.print("deserializeJson() failed with code");
    Serial.println(error.c_str());
  }
  
  String location = doc["cod"];
  String temperature = doc["list"][0]["main"]["temp"];
  String weather = doc["list"][0]["weather"][0]["main"];
  String description = doc["list"][0]["weather"][0]["description"];
  String idString = doc["list"][0]["weather"][0]["id"];
  String timeS = doc["list"][0]["dt_txt"];
  
  Serial.print("\nCity: ");
  Serial.print(location);
  Serial.print("\nTemperature: ");
  Serial.print(temperature);
  Serial.print("\nWeather: ");
  Serial.print(weather);
  Serial.print("\nDescription: ");
  Serial.print(description);
  weatherID = idString.toInt();
  Serial.print("\nWeatherID: ");
  Serial.print(weatherID);
  Serial.print("\nTime: ");
  Serial.print(timeS);

}
