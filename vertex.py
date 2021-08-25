class Vertex:
    def __init__(self, identity, y, x, value=float('inf')):
        self.identity = identity
        self.y = y
        self.x = x
        self.adjacent_vertices = []
        self.__value = value
        self.perv = None

    def get_id(self):
        return self.identity

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return other.identity == self.identity

    def __hash__(self) -> int:
        return hash(self.identity)

    def __lt__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__value < other.__value

    def __le__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__value <= other.__value

    def __gt__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__value > other.__value

    def __ge__(self, other):
        if not isinstance(other, Vertex):
            raise TypeError(str(other) + ' is not and instance of ' + self.__class__.__name__)
        return self.__value >= other.__value

    def __str__(self):
        return str(self.identity)

    def __repr__(self):
        return str(self.identity)