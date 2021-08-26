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

    # this function give us the list of shortest road between to vertices
    def find_shortest_path(self, start_id, end_id):
        
        edges = deepcopy(self.__edges)
        vertices = deepcopy(self.__vertices)
        heap = MinHeap(vertices)
        gereh_maghsad = heap[end_id]
        masir = []
        x_ha = []
        y_ha = []
        
        # giving the first vertice zero value
        heap.modify(start_id, 0)
        while end_id in heap:
            # removing the least value of vertices from list and putting it in v
            v = heap.pop()
            for hamsaye in v.adjacent_vertices:
                masir_ta_hamsaye = edges[v.identity, hamsaye.identity].get_weight()
                if v.value + masir_ta_hamsaye < hamsaye.value:
                    heap.modify(hamsaye.identity, v.value + masir_ta_hamsaye)
                    hamsaye.perv = v
                    
        while gereh_maghsad is not None:
            masir.append(gereh_maghsad)
            gereh_maghsad = gereh_maghsad.perv
        masir.reverse()
        return masir


a = Router(Constant.map_file)