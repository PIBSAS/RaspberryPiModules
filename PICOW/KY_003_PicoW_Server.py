from machine import Pin
from time import sleep
import network
import socket

class APModeLED:
    def __init__(self, ssid, password):
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid=ssid, password=password)
        self.ap.active(True)
        while not self.ap.active():
            pass
        print('AP Mode Is Active, You can Now Connect')
        print('IP Address To Connect to:', self.ap.ifconfig()[0])

        self.led = Pin("LED", Pin.OUT)
        self.sensor = Pin(22, Pin.IN)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)

    def web_page(self):
        return """<!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script>
                    function updateSensorValue() {
                        fetch('/sensor')
                            .then(response => response.text())
                            .then(data => {
                                document.getElementById('sensorValue').innerText = data;
                            });
                    }

                    setInterval(updateSensorValue, 1000);
                </script>
            </head>
            <body>
                <h1>KY-003: Hall Magnetic Sensor</h1>
                <p>Sensor Value: <span id="sensorValue"></span></p>
            </body>
            </html>"""

    def handle_request(self, conn, addr):
        request = conn.recv(1024).decode('utf-8')
        print('Got a connection from %s' % str(addr))
        print('Content = %s' % request)

        if request.find('GET /sensor') == 0:
            response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\nConnection: close\n\n' + str(self.sensor.value())
        elif request.find('GET / ') == 0:
            response = 'HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n' + self.web_page()
        else:
            response = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\nConnection: close\n\n'

        conn.send(response)
        conn.close()

    def run(self):
        while True:
            conn, addr = self.s.accept()
            self.handle_request(conn, addr)

            if self.sensor.value() == 1:
                self.led.on()
                print("ON")
            else:
                self.led.off()
                print("OFF")

            sleep(1)

# Replace 'PicoServer' and 'your_desired_password' with the desired SSID and password
ap_mode_led = APModeLED('PicoServer', 'your_desired_password')
ap_mode_led.run()
#End