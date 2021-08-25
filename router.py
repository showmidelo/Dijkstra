class Router:

    def __init__(self, map_file_address):
        self.__edges = {}
        self.__vertices = []
        v = {}
        self.map_file_address = map_file_address