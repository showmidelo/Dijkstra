class MinHeap:

    def __init__(self, array=[], index_table={}):
        self.__array = array
        self.__index_table = index_table
        self.make_heap()

    def make_heap(self):
        for i in range(len(self.__array) // 2).__reversed__():
            self.min_heapify(i)
        for index, vertex in enumerate(self.__array):
            self.__index_table[vertex.get_id()] = index

    def add(self, vertex):
        index = len(self.__array)
        self.__array.append(vertex)
        self.__index_table[vertex.get_id()] = index
        self.min_up_heapify(index)

    def remove(self, vertex_id, index=None):
        if index is None:
            index = self.__index_table[vertex_id]
        last_item = self.__array[-1]
        self.__index_table[last_item.get_id()] = index
        self.__array[index] = last_item

        del self.__index_table[vertex_id]
        del self.__array[-1]

        if len(self.__array) != 0:
            self.min_heapify(index)
            self.min_up_heapify(index)

    def modify(self, vertex_id, new_value):
        index = self.__index_table[vertex_id]
        self.__array[index].value = new_value
        self.min_up_heapify(index)
        self.min_heapify(index)

    def pop(self):
        root = self.__array[0]
        self.remove(self.__array[0].get_id(), 0)
        return root

    def min_heapify(self, i):
        # Makes a heap when the item with index i has a right and left
        # subtrees which both are heaps.
        le = self.left(i)
        ri = self.right(i)
        smallest = self.minimum(le, ri, i)
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def min_up_heapify(self, i):
        pa = self.parent(i)
        smallest = self.minimum(pa, i)
        if smallest != pa:
            self.swap(pa, i)
            self.min_up_heapify(pa)

    def right(self, i):
        ri = 2 * i + 2
        if ri < len(self.__array):
            return ri
        return i

    def left(self, i):
        ri = 2 * i + 1
        if ri < len(self.__array):
            return ri
        return i

    def parent(self, i):
        pa = (i - 1) // 2
        if pa < 0:
            return 0
        return pa

    def swap(self, i, j):
        temp = self.__array[i]
        self.__array[i] = self.__array[j]
        self.__array[j] = temp

        self.__index_table[self.__array[i].get_id()] = i
        self.__index_table[self.__array[j].get_id()] = j

    def minimum(self, *index):
        smallest = index[0]
        for i in index:
            if self.__array[i] < self.__array[smallest]:
                smallest = i
        return smallest

    def __str__(self):
        return self.__array.__str__()

    def __contains__(self, vertex_id):
        return vertex_id in self.__index_table

    def __getitem__(self, item):
        index = self.__index_table[item]
        return self.__array[index]

    def __setitem__(self, key, value):
        if key in self.__index_table:
            self.modify(key, value)
        else:
            self.add(value)

    def print(self):
        for i in self.__array:
            print(i)
        print(self.__index_table)
        print()
