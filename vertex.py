class Vertex:

    def __init__(self, identity, y, x, value=float('inf')):
        self.identity = identity
        self.y = y
        self.x = x
        self.adjacent_vertices = []
        self.__value = value
        self.perv = None