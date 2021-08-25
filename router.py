class Router:

    def __init__(self, map_file_address):
        self.__edges = {}
        self.__vertices = []
        v = {}
        self.map_file_address = map_file_address

        # open the file and reading lines of it
        with open(map_file_address, 'r') as MAP:
            n, m = [int(i) for i in MAP.readline().split()]