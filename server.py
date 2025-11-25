#!/usr/bin/env python3
"""Simple HTTP server to serve static files on port 3000."""

import http.server
import socketserver
import time

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
    time.sleep(1)
