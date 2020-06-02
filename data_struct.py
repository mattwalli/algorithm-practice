import unittest

class DoubleLinkedList:

    class Node:
        def __init__(self, data = None):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self, data = ()):
        self.head = None
        self.tail = None

        if len(data) == 0:
            return
        prev_node = None
        for d in data:
            new_node = self.Node(d)
            if self.head == None: # first node created
                self.head = new_node
            else: # existing nodes
                prev_node.next = new_node
                new_node.prev = prev_node
            prev_node = new_node # shift reference
        self.tail = prev_node # list creation done

    def __del__(self):
        
        def deep_del(node):
            if node.next != None: # not last node in list
                deep_del(node.next)
            del node
        
        if self.head != None: # there are nodes to delete
            deep_del(self.head)
    
    def get_values(self): # return a list of values head to tail
        ret = list()
        node = self.head
        while node != None:
            ret.append(node.data)
            node = node.next
        return ret

    def add_head(self, data = None):
        new_node = self.Node(data)
        if self.head == None: # empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = new_node

    def add_tail(self, data = None):
        new_node = self.Node(data)
        if self.tail == None: # empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node
            new_node.prev.next = new_node

class LinkedListTests(unittest.TestCase):

    def test_empty_list(self):
        data = DoubleLinkedList()
        self.assertEqual(data.get_values(), [])
        del data

    def test_create_list(self):
        data = DoubleLinkedList((1,2,3,4,5))
        self.assertEqual(data.get_values(), [1,2,3,4,5])
        del data
    
    def test_add_to_head(self):
        data = DoubleLinkedList()
        data.add_head(2)
        data.add_head(1)
        self.assertEqual(data.get_values(), [1,2])
        del data
    
    def test_add_to_tail(self):
        data = DoubleLinkedList()
        data.add_head(1)
        data.add_tail(2)
        self.assertEqual(data.get_values(), [1,2])
        del data

if __name__ == "__main__":
    unittest.main()
