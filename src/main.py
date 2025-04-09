import logging
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

SERVER_PORT = 8000


logger = logging.getLogger(__name__)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello world from hostname: " + socket.gethostname().encode())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    server = HTTPServer(("0.0.0.0", SERVER_PORT), SimpleHTTPRequestHandler)
    logger.info("Listening on port %d", SERVER_PORT)
    server.serve_forever()
