#!/usr/bin/env python3
import http.server
import os
import json
import time

class MyHandler(http.server.CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/events':
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            while True:
                data = readfile('/home/pi/Desktop/ioc_BOURAS/BDDtoWEB.txt')
                self.wfile.write(f"data: {json.dumps(data)}\n\n".encode('utf-8'$
                self.wfile.flush()
                time.sleep(1)
        else:
            super().do_GET()

def readfile(filename):
    if not os.path.isfile(filename):
        return {"lum": 0, "btn": 0}
    with open(filename, "r") as file:
        lines = file.readlines()
        lum = lines[0].split(": ")[1].strip().replace("%", "")
        btn = lines[1].split(": ")[1].strip()

PORT = 8000
httpd = http.server.HTTPServer(("", PORT), MyHandler)
print(f"Serving HTTP on port {PORT}")
httpd.serve_forever()
