"""
@author: Foschini Paolo
"""
import sys, signal
import http.server
import socketserver

server = socketserver.ThreadingTCPServer(('', 8080), http.server.SimpleHTTPRequestHandler)

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