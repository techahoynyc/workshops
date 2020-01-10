import board
import pulseio
import time
from adafruit_motor import servo
import busio
from digitalio import DigitalInOut
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests


#create a PWMOUT object on A2
pwm = pulseio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)

#create a servo object my servo
my_servo = servo.Servo(pwm)
my_servo.angle = 0
#my_servo.angle = 110
print("ESP32 SPI webclient test")

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"

JSON_URL = "http://api.openweathermap.org/data/2.5/forecast?id=5103269&APPID=b15c688176e185870b804efe9d71de3c&units=imperial"

PARKING_URL = "https://raw.githubusercontent.com/techahoynyc/workshops/master/coding-in-arduino-ambient-computing/nycasp/parkingDays.json"

# If you are using a board with pre-defined ESP32 Pins:
#esp32_cs = DigitalInOut(board.ESP_CS)
#esp32_ready = DigitalInOut(board.ESP_BUSY)
#esp32_reset = DigitalInOut(board.ESP_RESET)

# If you have an externally connected ESP32:
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

requests.set_socket(socket, esp)

#if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    #print("ESP32 found and in idle mode")
#("Firmware vers.", esp.firmware_version)
#print("MAC addr:", [hex(i) for i in esp.MAC_address])


for ap in esp.scan_networks():
    print("\t%s\t\tRSSI: %d" % (str(ap['ssid'], 'utf-8'), ap['rssi']))


#print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP('techahoy', 'makerspace')
    except RuntimeError as e:
        #print("could not connect to AP, retrying: ",e)
        continue

print("Connected to", str(esp.ssid, 'utf-8'), "\tRSSI:", esp.rssi)
print("My IP address is", esp.pretty_ip(esp.ip_address))

r1 = requests.get("http://worldclockapi.com/api/json/est/now")
dateStuff = r1.json()
rawDate = dateStuff["currentDateTime"]
rawDate = rawDate[:10]
print(rawDate)
rawDate2 = "2020-02-12"

r2 = requests.get(PARKING_URL)
info = r2.json()

for date in range(len(info)):
    for k in info[date]:
        #print(k)
        if rawDate2 == k:
            print(k)
            print("Parking Suspended")


'''
print("IP lookup adafruit.com: %s" % esp.pretty_ip(esp.get_host_by_name("adafruit.com")))
print("Ping google.com: %d ms" % esp.ping("google.com"))
'''
#esp._debug = True
'''
print("Fetching text from", TEXT_URL)
r = requests.get(TEXT_URL)
print('-'*40)
print(r.text)
print('-'*40)
r.close()
'''

'''
print()
print("FETCHING WEATHER DATA FROM", JSON_URL)
r = requests.get(JSON_URL)
print('-'*40)


info = r.json()
print(info["city"]["name"])
print(info["city"]["coord"])

for i in range(0,len(info["list"])):
    print(info["list"][i]["dt_txt"])
    print('-'*40)
    print('-'*40)

'''
'''
temp = int(r.json()["list"][0]["main"]["temp"])
print(temp)
time.sleep(5)
if int(temp) < 42:
    my_servo.angle = 90
    print(temp)
    print("ITS FREEEEEZING!!!!!!!")

print('-'*40)
r.close()
'''
print("Done!")