from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"serv")

# Настройка и запуск сервера
def run(host="localhost", port=4443, certfile="cert.pem", keyfile="key.pem"):
    # Создаём HTTP-сервер
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHandler)
    
    # Настройка SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"Сервер запущен https://{host}:{port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
