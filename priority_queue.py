class PQ:
    def __init__(self, array = []):
        self.heap = list()
        if len(array) != 0:
            while len(array) > 0:
                self.insert(array.pop())

    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def get_max(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    def del_max(self):
        m = self.get_max()
        if m != None:
            self.heap[0] = self.heap.pop()
            self.__sift_down(1)
        return m
    
    def insert(self, key):
        self.heap.append(key)
        self.__sift_up(self.size())
    
    def __sift_down(self, i):
        while i * 2 <= self.size():
            j = i * 2
            if j < self.size() and self.heap[j - 1] < self.heap[j]:
                j += 1
            if self.heap[i - 1] >= self.heap[j - 1]:
                break
            self.heap[i - 1], self.heap[j - 1] = self.heap[j - 1], self.heap[i - 1]
            i = j
    
    def __sift_up(self, i):
        while i > 1:
            j = i // 2
            if self.heap[j - 1] >= self.heap[i - 1]:
                break
            self.heap[i - 1], self.heap[j - 1] = self.heap[j - 1], self.heap[i - 1]
            i = j