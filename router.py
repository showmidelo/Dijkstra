from vertex import *
from edge import *
from heap import *
from copy import deepcopy
from constant import *


class Router:
    def __init__(self, map_file_address):
        self.__edges = {}
        self.__vertices = []
        v = {}
        self.map_file_address = map_file_address

        # open the file and reading lines of it
        with open(Constant.map_file, 'r') as MAP:
            n, m = [int(i) for i in MAP.readline().split()]
            
        # reading vertex
            for i in range(n):
                identity, y, x = (float(i) for i in MAP.readline().split())
                identity = int(identity)
                vertex = Vertex(identity, y, x)
                self.__vertices.append(vertex)
                v[identity] = vertex
                
        # reading edges and add adjacent_vertices
            for i in range(m):
                id1, id2 = (int(i) for i in MAP.readline().split())
                edge = Edge(v[id1], v[id2])
                self.__edges[id1, id2] = edge
                self.__edges[id2, id1] = edge
                v[id1].adjacent_vertices.append(v[id2])
                v[id2].adjacent_vertices.append(v[id1])

    # this function give us the list of shortest road between two vertices
    def find_shortest_path(self, start_id, end_id):

        edges = deepcopy(self.__edges)
        vertices = deepcopy(self.__vertices)
        heap = MinHeap(vertices)
        last_knot = heap[end_id]
        road = []

        # giving the first vertice zero value
        heap.modify(start_id, 0)

        while end_id in heap:
            # removing the least value of vertices from list and putting it in "least_value_vertice"
            least_value_vertice = heap.pop()

            # calculate the next vertice for moving to it in the shortest way
            for adjacent in least_value_vertice.adjacent_vertices:
                road_to_adjacent = edges[least_value_vertice.identity, adjacent.identity].get_weight()
                if least_value_vertice.value + road_to_adjacent < adjacent.value:
                    heap.modify(adjacent.identity, least_value_vertice.value + road_to_adjacent)
                    adjacent.perv = least_value_vertice

        # this loop add the vertices that have been covered to the "road" list
        while last_knot is not None:
            road.append(last_knot)
            last_knot = last_knot.perv
        road.reverse()
        return road


a = Router(Constant.map_file)

