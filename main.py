import machine as m
from ssd1306 import SSD1306_I2C
import time
import network
import socket
import sys
import applejuice
import random
import bluetooth as bt
import ujson as json
import ucolorama
import logging as l

l.logging_level = 1

l.blacklist = [
    "CNSL/LOG",
    "CNSL/MENU"
]

class s:
    pass

with open("settings.json", "r") as file:
    s = json.loads(file.read())

# Interrupts +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class interrupt:
    def emergency_reset():
        l.debug("IRQERESET", "Check")
        if b.left.value() == 1:
            l.debug("IRQERESET", "Wait")
            old_time = time.ticks_ms()
            b.released(b.back)
            l.debug("IRQERESET", "Verify")
            if time.ticks_ms()-1000 > old_time:
                l.debug("IRQERESET", "Confirm")
                l.info("POWER", "Hard Reset")
                m.reset()
        else:
            l.debug("IRQERESET", "Cancel")

i2c = m.I2C(0, sda=4, scl=5, freq=200000)
devices = i2c.scan()

class b:
    up = m.Pin(10, m.Pin.IN, m.Pin.PULL_DOWN)
    down = m.Pin(11, m.Pin.IN, m.Pin.PULL_DOWN)
    left = m.Pin(12, m.Pin.IN, m.Pin.PULL_DOWN)
    right = m.Pin(13, m.Pin.IN, m.Pin.PULL_DOWN)
    ok = m.Pin(14, m.Pin.IN, m.Pin.PULL_DOWN)
    back = m.Pin(15, m.Pin.IN, m.Pin.PULL_DOWN)
    class wait:
        def pressed(pin):
            while pin.value() == 0: pass
        def released(pin):
            while pin.value() == 1: pass
        def bumped(pin):
            while pin.value() == 0: pass
            while pin.value() == 1: pass
        def pressed_any():
            while True:
                if b.up.value() == 1: break
                if b.down.value() == 1: break
                if b.left.value() == 1: break
                if b.right.value() == 1: break
                if b.ok.value() == 1: break
                if b.back.value() == 1: break
        def released_any():
            if b.up.value() == 1:
                b.wait.released(b.up)
                return
            if b.down.value() == 1:
                b.wait.released(b.down)
                return
            if b.left.value() == 1:
                b.wait.released(b.left)
                return
            if b.right.value() == 1:
                b.wait.released(b.right)
                return
            if b.ok.value() == 1:
                b.wait.released(b.ok)
                return
            if b.back.value() == 1:
                b.wait.released(b.back)
                return
        def bumped_any():
            b.wait.pressed_any()
            b.wait.released_any()

#b.back.irq(trigger=m.Pin.IRQ_RISING, handler=interrupt.emergency_reset())

led = m.Pin("LED", m.Pin.OUT)
led.on()

oled = SSD1306_I2C(128, 64, i2c)

logs = [
    "",
    "",
    "",
    "",
    ""
]

logs_title = ""

menu_items = []
menu_selection = 0
menu_title = ""
selected = ""

class os:
    class path:
        def isfile(file) -> bool:
            try:
                with open(file, "r") as f: pass
                return True
            except:
                return False

class console:
    mode = "logs"
    def clear() -> None:
        oled.fill(0)
        oled.show()
    def update_logs(title: str, logs: list[str]) -> None:
        oled.fill(0)
        oled.text(title, 0, 4)
        oled.text(logs[0], 0, 16)
        oled.text(logs[1], 0, 26)
        oled.text(logs[2], 0, 36)
        oled.text(logs[3], 0, 46)
        oled.text(logs[4], 0, 56)
        oled.show()
    def update_menu(selection: int, items: list[str], title: str) -> None:
        oled.fill(0)
        oled.text(title, 0, 4)
        oled.text(f"  {items[selection-2] if selection-2 >= 0 and selection-2 < len(items) else ""}", 0, 16)
        oled.text(f"  {items[selection-1] if selection-1 >= 0 and selection-1 < len(items) else ""}", 0, 26)
        oled.text(f"> {items[selection] if selection >= 0 and selection < len(items) else ""}", 0, 36)
        oled.text(f"  {items[selection+1] if selection+1 >= 0 and selection+1 < len(items) else ""}", 0, 46)
        oled.text(f"  {items[selection+2] if selection+2 >= 0 and selection+2 < len(items) else ""}", 0, 56)
        oled.show()
    def log(log: str, title: str, logs: list[str]) -> None:
        l.info("CNSL/LOG", log)
        logs.pop(0)
        logs.append(log)
        logs_title = title
        if console.mode == "logs":
            console.update_logs(logs_title, logs)
    def reset_logs() -> list[str]:
        return [
            "",
            "",
            "",
            "",
            ""
        ]
    def set_mode(mode: Literal["menu", "logs"]):
        if not mode in ["menu", "logs"]:
            raise ValueError(f"\"{mode}\" is not a valid option")
        console.mode = mode
        if mode == "logs":
            console.update_logs(logs_title, logs)
        if mode == "menu":
            console.update_menu(menu_selection, menu_items, menu_title)
    def handle_menu(title, items, selection):
        l.debug("CNSL/MENU", "Update menu")
        console.update_menu(selection, items, title)
        l.debug("CNSL/MENU", "Start forever loop")
        while True:
            l.debug("CNSL/MENU", "Wait for any key")
            b.wait.pressed_any()
            if b.up.value() == 1:
                l.debug("CNSL/MENU", "Pressed up")
                b.wait.released(b.up)
                if selection > 0:
                    selection -= 1
                else:
                    selection = len(items)-1
            if b.down.value() == 1:
                l.debug("CNSL/MENU", "Pressed down")
                b.wait.released(b.down)
                if selection < len(items)-1:
                    selection += 1
                else:
                    selection = 0
            if b.back.value() == 1:
                l.debug("CNSL/MENU", "Pressed back")
                b.wait.released(b.back)
                return ""
            if b.ok.value() == 1:
                l.debug("CNSL/MENU", "Pressed ok")
                b.wait.released(b.ok)
                return items[selection]
            console.update_menu(selection, items, title)

class p:
    class load:
        current = 0
        modifier = 0.1
        change = 100 / 1
    def to_number(percentage, modifier) -> int:
        return int(percentage * modifier)
    def show_percentage() -> str:
        return f"{int(p.load.current)}%{" " * (4 - len(str(int(p.load.current))))}{"#" * int(p.load.current * p.load.modifier)}{"-" * (10 - int(p.load.current * p.load.modifier))}"

class wifi:
    available = False
    ssid = "robotica"
    pkey = "77SERVER"
    wlan = 0
    wait = 0
    max_wait = 10
    addr = 0
    socket = 0
    request = 0
    request_type = 0
    
    ctypes = {
        "html"  : "text/html",
        "css"   : "text/css",
        "js"    : "text/javascript",
        "png"   : "image/png",
        "jpeg"  : "image/jpeg",
        "gif"   : "image/gif",
        "ico"   : "image/x-icon",
        "mp3"   : "audio/mpeg",
        "wav"   : "audio/x-wav",
        "ogg"   : "application/ogg",
        "json"  : "application/json",
        "zip"   : "application/zip",
        "xml"   : "application/xml",
        "pdf"   : "application/pdf"
    }

class bluetooth:
    available = False
    interface = 0

# APPS ********************************************************************************************************************************************************

class apps:
    class bluetooth:
        def enable(status):
            bluetooth.interface = bt.BLE()
            bluetooth.interface.active(status)
            bluetooth.available = bluetooth.interface.active()
        def handle_enabling(status):
            l.info("BLE", "Initialize Bluetooth")
            console.log(f"Init BLE", f"{p.show_percentage()}", logs)
            if s["bluetooth"]["enabled"] == True:
                apps.bluetooth.enable(True)
                if bluetooth.available == False:
                    l.warn("BLE", "Could not initialize Bluetooth")
                    console.log(f"BLE Error", f"{p.show_percentage()}", logs)
                    return 1
                else:
                    l.info("BLE", "Bluetooth initialized")
                    console.log(f"BLE Ok", f"{p.show_percentage()}", logs)
                    return 0
            else:
                bluetooth.interface = None
                bluetooth.available = False
                l.warn("BLE", "Bluetooth has been disabled in the config")
                console.log(f"BLE Disabled", f"{p.show_percentage()}", logs)
                return -1
        class applejuice:
            def main():
                console.set_mode("menu")
                while True:
                    menu_title = "...th/AppleJuice"
                    menu_selection = 0
                    menu_items = ["Random"]
                    for item in applejuice.payload_names:
                        menu_items.append(item)
                    selected = console.handle_menu(menu_title, menu_items, menu_selection)
                    if selected == "":
                        selected = 0
                        break
                    if selected == "Random":
                        logs = console.reset_logs()
                        console.set_mode("logs")
                        console.log("Start GAP ADs", "AppleJuice", logs)
                        while True:
                            if b.back.value() == 1:
                                break
                            bluetooth.interface.gap_advertise(int(0.2 * 1000000), adv_data=random.choice(list(applejuice.payload_names.values()))) # interval is in microseconds
                            time.sleep(1)
                            console.log("Shuffle GAP ADs", "AppleJuice", logs)
                        console.log("Stop GAP ADs", "AppleJuice", logs)
                        bluetooth.interface.gap_advertise(None)
                        continue
                    else:
                        logs = console.reset_logs()
                        console.set_mode("logs")
                        console.log("Start GAP ADs", "AppleJuice", logs)
                        bluetooth.interface.gap_advertise(int(0.2 * 1000000), adv_data=applejuice.payload_names[selected])
                        b.wait.bumped(b.back)
                        console.log("Stop GAP ADs", "AppleJuice", logs)
                        bluetooth.interface.gap_advertise(None)
                        continue

    class wifi:
        def enable_sta_if():
            wifi.wlan = network.WLAN(network.STA_IF)
            wifi.wlan.active(True)
            wifi.wlan.connect(wifi.ssid, wifi.pkey)
            while wifi.wait < wifi.max_wait:
                if wifi.wlan.status() < 0 or wifi.wlan.status() >= 3:
                    break
                wifi.wait += 1
                time.sleep(1)
        def handle_enabling_sta_if():
            console.set_mode("logs")
            l.info("WIFI", "Initialize WiFi in Station mode")
            console.log(f"Connect to WiFi", f"Enable WiFi", logs)
            apps.wifi.enable_sta_if()
            if wifi.wlan.status() != 3:
                l.info("WIFI", f"Could not initialize WiFi [{wifi.wlan.status()}]")
                console.log(f"WiFi error", f"Enable WiFi", logs)
                wifi.available = False
            else:
                l.info("WIFI", "WiFi initialized")
                console.log(f"WiFi ok", f"Enable WiFi", logs)
                wifi.available = True
            l.info("WIFI", f"Current IP address: {wifi.wlan.ifconfig()[0]}")
            console.log(f"IP {wifi.wlan.ifconfig()[0] if wifi.available else "Not available"}", f"Not available", logs)
        class example_server:
            def main():
                console.set_mode("logs")
                l.info("WIFI/SOCK", "Start web server")
                console.log(f"Start web server", f"{p.show_percentage()}", logs)
                wifi.addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
                wifi.socket = socket.socket()
                wifi.socket.bind(wifi.addr)
                wifi.socket.listen(1)

                l.info("WIFI/SOCK", "Socket is listening for new incoming connections")
                console.log(f"Socket listening", f"{p.show_percentage()}", logs)

                while True:
                    try:
                        wifi.client, wifi.addr = wifi.socket.accept()
                        wifi.request = wifi.client.recv(1024)
                        wifi.request = str(wifi.request)
                        wifi.request = wifi.request.split(" HTTP/")[0].split(" ", 1)[1]
                        if wifi.request.endswith("/"):
                            wifi.request += "index.html"

                        console.log(f"CC {wifi.request}", f"{wifi.addr[0]}", logs)
                        l.info("WIFI/STA", f"User {wifi.addr[0]} requested /web{wifi.request}")
                        request_code = 200
                        if not os.path.isfile(f"/web{wifi.request}"):
                            request_code = 404
                        if request_code == 200:
                            with open(f"/web{wifi.request}", "r") as html:
                                content = html.read()
                                content_type = wifi.ctypes[wifi.request.split(".")[-1]]
                        else:
                            with open("/web/404.html", "r") as html:
                                content = html.read()
                                content_type = wifi.ctypes["html"]
                        
                        wifi.client.send(f"HTTP/1.0 {request_code} OK\r\nContent-type: {content_type}\r\n\r\n")
                        wifi.client.send(f"{content}")
                        wifi.client.close()
                    except OSError as e:
                        wifi.client.close()
                        raise e

p.load.current = 0

# MENU --------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    console.log(f"Boot up", f"{p.show_percentage()}", logs)
    p.load.current += p.load.change

    console.log(f"PRESS @ TO START", f"{p.show_percentage()}", logs)

    led.off()

    b.wait.bumped(b.ok)

    while True:
        menu_items = [
            "Apps",
            "Standby",
            "Settings",
            "Restart",
        ]
        menu_title = "Welcome!"
        menu_selection = 0

        console.set_mode("menu")

        selected = console.handle_menu(menu_title, menu_items, menu_selection)
        if selected == "Apps":
            while True:
                menu_items = ["Bluetooth", "WiFi"]
                menu_title = "Apps"
                menu_selection = 0
                selected = console.handle_menu(menu_title, menu_items, menu_selection)
                if selected == "Bluetooth":
                    while True:
                        menu_items = ["AppleJuice"]
                        menu_title = "Apps/Bluetooth"
                        menu_selection = 0
                        selected = console.handle_menu(menu_title, menu_items, menu_selection)
                        if selected == "AppleJuice":
                            console.set_mode("logs")
                            apps.bluetooth.handle_enabling(True)
                            if bluetooth.available:
                                apps.bluetooth.applejuice.main()
                                console.set_mode("menu")
                            else:
                                oled.fill(0)
                                oled.text("Not available", 0, 4)
                                oled.text("initialization", 0, 16)
                                oled.text("error", 0, 26)
                                oled.show()
                                time.sleep(1)
                            continue
                        if selected == "":
                            selected = 0
                            break
                if selected == "WiFi":
                    while True:
                        menu_items = ["Example Server"]
                        menu_title = "Apps/WiFi"
                        menu_selection = 0
                        selected = console.handle_menu(menu_title, menu_items, menu_selection)
                        if selected == "Example Server":
                            apps.wifi.handle_enabling_sta_if()
                            if wifi.available:
                                apps.wifi.example_server.main()
                                console.set_mode("menu")
                            else:
                                oled.fill(0)
                                oled.text("Not available", 0, 4)
                                oled.text("initialization", 0, 16)
                                oled.text("error", 0, 26)
                                oled.show()
                                time.sleep(1)
                            continue
                        if selected == "":
                            selected = 0
                            break
                if selected == "":
                    selected = 0
                    break

        if selected == "Standby":
            console.clear()
            b.wait.bumped_any()
            continue
        if selected == "Restart":
            while True:
                menu_items = ["Soft Reset", "Hard Reset"]
                menu_title = "Restart"
                menu_selection = 0
                selected = console.handle_menu(menu_title, menu_items, menu_selection)
                if selected == "Soft Reset":
                    l.info("POWER", "Soft Reset")
                    console.clear()
                    sys.exit()
                    while True: pass
                if selected == "Hard Reset":
                    l.info("POWER", "Hard Reset")
                    console.clear()
                    m.reset()
                    while True: pass
                if selected == "":
                    selected = 0
                    break

except OSError as e:
    console.log(f"{str(e).replace("Errno ", "")}", f"Fatal Error", logs)
    console.log(f"PRESS x TO RESET", "Fatal Error", logs)
    b.wait.bumped(b.back)
    console.clear()
    m.reset()