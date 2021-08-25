from socket import socket
from threading import Thread
from router import *
import time


class Server:
    def __init__(self):
        self.router = Router(Constant.map_file)

    def start(self):
        with socket() as welcoming_socket:
            welcoming_socket.bind(('', 8000))
            welcoming_socket.listen()
            print("waiting for someone to connect...")
            while True:
                client_socket, address = welcoming_socket.accept()
                Thread(target=self.client_handler, args=(client_socket,)).start()

    def client_handler(self, sock: socket):
        sock.send(Constant.map_file.encode('ascii'))
        try:
            while True:
                a, _ = sock.recvfrom(2048)
                a = a.decode("ascii")
                print(a)
                b, c = a.split()
                d = self.router.find_shortest_path(int(b), int(c))
                strings = [str(i) for i in d]
                sock.send(" ".join(strings).encode("ascii"))
                time.sleep(1)
        except Exception:
            pass


s = Server()
s.start()