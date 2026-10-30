
import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"Lab honeypot listening on {HOST}:{PORT}")

try:
    while True:
        conn, addr = server.accept()

        print("Connection detected:", addr)
        print("Time:", datetime.now())

        conn.sendall(b"Lab service: connection logged.\n")
        conn.close()
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
finally:
    server.close()
