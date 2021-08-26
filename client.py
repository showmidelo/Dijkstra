from socket import socket
from router import *
import matplotlib.pyplot as plt
from vertex import *
from edge import *


class Client:

    def __init__(self):
        self.__edges = {}
        self.__vertices = []
        v = {}

        with socket() as sock:
            sock.connect(('127.0.0.1', 8000))
            # receive what server has sent client
            b = sock.recv(2048).decode('ascii')
            self.router = Router(str(b))
            # input two numbers for using in the find shortest path function
            a = input("Enter two number: ")
            f, g = a.split()
            masir = self.router.find_shortest_path(int(f), int(g))
            # send two inputted numbers to server
            sock.send(a.encode('ascii'))
            # receive the road list that server has sent us
            c = sock.recv(2048).decode("ascii")
            print(c)

            with open(b, 'r') as MAP:
                n, m = [int(i) for i in MAP.readline().split()]
                # reading till n line and add them to list (self.__vertices)
                for i in range(n):
                    identity, y, x = (float(i) for i in MAP.readline().split())
                    identity = int(identity)
                    vertex = Vertex(identity, y, x)
                    self.__vertices.append(vertex)
                    v[identity] = vertex

                # reading lines between n and m and add items to dictionary (self.__edges)
                for i in range(m):
                    id1, id2 = (int(i) for i in MAP.readline().split())
                    edge = Edge(v[id1], v[id2])
                    self.__edges[id1, id2] = edge
                    self.__edges[id2, id1] = edge
                    v[id1].adjacent_vertices.append(v[id2])
                    v[id2].adjacent_vertices.append(v[id1])
                # plot the map and draw what client wants
                fig, ax = plt.subplots(nrows=1, ncols=1)
                fig.set_facecolor('#FFFFFF')
                # cause we have duplicate items in dictionary we use this trick to remove them
                Zoj = True
                for yal in self.__edges:
                    if Zoj:
                        x1 = self.__edges[yal].head().x
                        y1 = self.__edges[yal].head().y
                        x2 = self.__edges[yal].tail().x
                        y2 = self.__edges[yal].tail().y
                        plt.plot([x1, x2], [y1, y2], marker='o', color='#d8d8d8')
                        plt.annotate(str(self.__edges[yal].head().identity), (x1, y1))
                        plt.annotate(str(self.__edges[yal].tail().identity), (x2, y2))
                    Zoj = not Zoj
                x_ha = []
                y_ha = []
                # plot the road between two numbers (or vertices)  that client gave us
                for e in masir:
                    x_ha.append(e.x)
                    y_ha.append(e.y)
                plt.plot(x_ha, y_ha, marker='o', color='#FC33FF')
                plt.show()


A = Client()
