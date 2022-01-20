import senko
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'LittleBird_Private'
password = 'LBRocks!IoT'

routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect(ssid,password)
routercon = network.WLAN(network.STA_IF)

print('Connection successful')

OTA = senko.Senko(user = "quintajm",
                  repo="SenkoTest",
                  branch="main",
                  files = ["boot.py","main.py","servo_control.py","senko.py"]
                  )

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()
