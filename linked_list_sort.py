from timeit import timeit
from random import randint

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
    
    def clear(self):
        this_node = self.head
        self.head = None
        while this_node != None:
            next_node = this_node.next
            del this_node
            this_node = next_node
    
    def print(self):
        point = self.head
        while point != None:
            print(f"{point.value}, ", end="")
            point = point.next
        print("<END>")
    
    def fill_random(self, n, a, b):
        if self.head != None:
            self.clear()
        if n <= 0:
            return
        self.head = point = self.Node(randint(a, b))
        for i in range(1, n):
            point.next = self.Node(randint(a, b))
            point = point.next
    
    def is_sorted(self):
        if self.head == None:
            return True
        point = self.head
        while point.next != None:
            if point.value > point.next.value:
                return False
            point = point.next
        return True
    
    def merge(self, low, mid, high):
        point1, point2 = low, mid
        if point1.value < point2.value:
            new_head = point1
            new_tail = point1
            point1 = point1.next
        else:
            new_head = point2
            new_tail = point2
            point2 = point2.next
        while point1 != mid or point2 != high:
            if point1 == mid:
                new_tail.next = point2
                new_tail = point2
                point2 = point2.next
            elif point2 == high:
                new_tail.next = point1
                new_tail = point1
                point1 = point1.next
            elif point1.value < point2.value:
                new_tail.next = point1
                new_tail = point1
                point1 = point1.next
            else:
                new_tail.next = point2
                new_tail = point2
                point2 = point2.next
        new_tail.next = high
        return new_head, new_tail
    
    def merge_sort(self):
        size = 1
        while True:
            low = self.head
            while True:
                #self.print()
                mid = low
                for a in range(size):
                    mid = mid.next
                    if mid == None:
                        break
                if mid == None:
                    if low == self.head:
                        return
                    size *= 2
                    break
                high = mid
                for a in range(size):
                    high = high.next
                    if high == None:
                        break
                if low == self.head:
                    self.head, new_tail = self.merge(low, mid, high)
                else:
                    new_head = new_tail
                    new_head.next, new_tail = self.merge(low, mid, high)
                if high == None:
                    size *= 2
                    break
                low = high

llist = LinkedList()
llist.fill_random(800000, 0, 1000000)
print("Sorting...")
exec_time = timeit('llist.merge_sort()', number=1, globals=globals())
print(f"Execution time: {exec_time} seconds")
print(f"Is sorted: {llist.is_sorted()}")
llist.clear()