#!/usr/bin/env python3
"""Production HTTP server for Railway deployment.

Railway provides HTTPS automatically, so this serves over HTTP.
"""

import http.server
import os

PORT = int(os.environ.get("PORT", 8080))

handler = http.server.SimpleHTTPRequestHandler

with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
