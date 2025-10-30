# app/app.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(b"hello from sample app\n")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    print("listening on :8080")
    server.serve_forever()

