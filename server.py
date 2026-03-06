#!/usr/bin/env python3
"""Simple HTTPS server for local development."""

import http.server
import ssl

PORT = 8443

handler = http.server.SimpleHTTPRequestHandler

with http.server.HTTPServer(("", PORT), handler) as httpd:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Serving HTTPS on https://localhost:{PORT}")
    httpd.serve_forever()
