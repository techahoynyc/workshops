# ESP32 - Weather
The [Adafruit HUZZAH32](https://learn.adafruit.com/adafruit-huzzah32-esp32-feather) is a great chip for your next [IoT](https://en.wikipedia.org/wiki/Internet_of_things) project.

## Workshop Details
* The ESP32 is the next iteration of the popular ESP8266.  Both chips provide low-cost WiFi connectivity allowing your microcontroller projects to interact with the Internet.
* We have included several of reference links below which we relied upon while creating this workshop.

## Notes:
* The config.h header file, referenced in [huzzah32-weather.ino], contains private/sensative information (i.e. Wifi SSID/Password and OpenWeather API Key) that should not be publicly shared and is intentionally excluded from this repository.  Therefore, you must manually create the config.h file with the following format.  
```
#define WIFI "your_ssid"
#define PASS "your_ssid_password"
#define MYCITY "your_city"
#define OWAPI "your_openweather_apikey"
```

## Reference Links
* OpenWeather API Documentation - https://openweathermap.org/forecast5#limit
* OpenWeather Weather Condition Codes - https://openweathermap.org/weather-conditions
* Simple Arduino sketch to connect ESP32 to wifi - https://techtutorialsx.com/2017/05/19/esp32-http-get-requests/
* Free online JSON viewer (for readability) - https://codebeautify.org/jsonviewer
* DeserializeJSON Documentation - https://arduinojson.org/v6/api/json/deserializejson/
* DeserializeJSON Error Documentation - https://arduinojson.org/v6/api/misc/deserializationerror/
* ArduinoJson Assistant - https://arduinojson.org/v6/assistant/
*(Optional)*  
* NTP Time - https://lastminuteengineers.com/esp32-ntp-server-date-time-tutorial/
* Unix Epoch Time Converter - https://www.epochconverter.com/


## BOM
|Item|URL|
|---|---|
|Adafruit HUZZAH32 |https://www.adafruit.com/product/3405 |
|Breadboard|https://www.amazon.com/gp/product/B07LFD4LT6/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1 |
|Alligator Clips|https://www.amazon.com/gp/product/B07FMBGC3X/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1 |
