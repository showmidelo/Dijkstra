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
                data, _ = sock.recvfrom(2048)
                data = data.decode("ascii")
                print(data)
                first_vertice, second_vertice = data.split()
                roads = self.router.find_shortest_path(int(first_vertice), int(second_vertice))
                strings = [str(road) for road in roads]
                sock.send(" ".join(strings).encode("ascii"))
                time.sleep(1)
        except Exception:
            pass


s = Server()
s.start()