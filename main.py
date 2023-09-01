from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, world!')
        else:
            # For all other requests, serve files normally
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # Get the size of data
        post_data = self.rfile.read(content_length)  # Get the data
        post_data_json = json.loads(post_data.decode('utf-8'))

        print(f"Received data: {post_data.decode('utf-8')}")

        # Echo back the received data as a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(post_data_json["challenge"].encode('utf-8'))


PORT = 3000
with TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()
