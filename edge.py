class Edge:
    
    def __init__(self, head, tail):
        self.__head = head
        self.__tail = tail
        self.weight = 0

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def get_weight(self):
        x1 = self.__head.x
        y1 = self.__head.y
        x2 = self.__tail.x
        y2 = self.__tail.y
        x = (x1 - x2) ** 2
        y = (y1 - y2) ** 2
        Fisaghores = (x + y) ** 0.5
        Length = Fisaghores
        return Length

    def __str__(self):
        return "(" + str(self.__head.identity) + "-->" + str(self.__tail.identity) + ")"

    def __repr__(self):
        return "(" + str(self.__head.identity) + "-->" + str(self.__tail.identity) + ")"