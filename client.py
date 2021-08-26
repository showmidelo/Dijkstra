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
            map = sock.recv(2048).decode('ascii')
            self.router = Router(str(map))
            # input two numbers for using in the find shortest path function
            inputs = input("Enter two number: ")
            first_vertice, second_vertice = inputs.split()
            path = self.router.find_shortest_path(int(first_vertice), int(second_vertice))
            # send two inputted numbers to server
            sock.send(inputs.encode('ascii'))
            # receive the road list that server has sent us
            roads = sock.recv(2048).decode("ascii")
            print(roads)

            with open(map, 'r') as MAP:
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
                Even = True
                for edge in self.__edges:
                    if Even:
                        x1 = self.__edges[edge].head().x
                        y1 = self.__edges[edge].head().y
                        x2 = self.__edges[edge].tail().x
                        y2 = self.__edges[edge].tail().y
                        plt.plot([x1, x2], [y1, y2], marker='o', color='#d8d8d8')
                        plt.annotate(str(self.__edges[edge].head().identity), (x1, y1))
                        plt.annotate(str(self.__edges[edge].tail().identity), (x2, y2))
                    Even = not Even
                xs = []
                ys = []
                # plot the road between two numbers (or vertices)  that client gave us
                for road in path:
                    xs.append(road.x)
                    ys.append(road.y)
                plt.plot(xs, ys, marker='o', color='#FC33FF')
                plt.show()


A = Client()
