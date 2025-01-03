import logging
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Handling request: {self.path}")
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Welcome to My Custom Server</h1>")
        else:
            self.send_error(404, "Page not found")

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)  # Listen on all interfaces
    httpd = HTTPServer(server_address, MyHandler)
    logging.info("Server started at http://localhost:8080")
    httpd.serve_forever()
