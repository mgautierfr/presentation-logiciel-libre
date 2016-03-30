#!/usr/bin/env python3

import http.server
import socketserver
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
webbrowser.open('http://localhost:{}/index.html'.format(PORT))
try:
    httpd.serve_forever()
except:
    # Probably not needed, but.. anyway
    httpd.shutdown()
