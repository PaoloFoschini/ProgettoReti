"""
@author: Foschini Paolo
"""
import sys, signal
import http.server
import socketserver

import http.server

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/www/index.html')
            self.end_headers()
        else:
            super().do_GET()

server = socketserver.ThreadingTCPServer(('', 8080), CustomRequestHandler)

server.daemon_threads = True  
server.allow_reuse_address = True  

def signal_handler(signal, frame):
    print('Exiting http server (Ctrl+C pressed)')
    try:
      if (server):
          server.server_close()
    finally:
      sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
  while True:
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close()