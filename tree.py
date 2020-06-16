class BST:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.n = 1
            self.left = None
            self.right = None
    
    def __init__(self):
        self.__root = None

    def size(self):
        return self.__size(self.__root)
    
    def __size(self, node):
        if node == None:
            return 0
        return node.n
    
    def get(self, key):
        return self.__get(self.__root, key)
    
    def __get(self, node, key):
        if node == None:
            return None
        if node.key > key:
            return self.__get(node.left, key)
        if node.key < key:
            return self.__get(node.right, key)
        return node.value
    
    def put(self, key, value):
        self.__root = self.__put(self.__root, key, value)

    def __put(self, node, key, value):
        if node == None:
            return self.Node(key, value)
        if node.key > key:
            node.left = self.__put(node.left, key, value)
        elif node.key < key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value
        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def __delete(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.__delete(node.left, key)
        elif node.key < key:
            node.right = self.__delete(node.right, key)
        else:
            if node.left == None:
                temp_node = node.right
                del node
                return temp_node
            if node.right == None:
                temp_node = node.left
                del node
                return temp_node
            temp_node = node.right
            while temp_node.left != None:
                temp_node = temp_node.left
            temp_node.left = node.left
            temp_node.right = self.__delmin(node.right)
            del node
            node = temp_node
        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def __delmin(self, node):
        if node.left == None:
            return node.right
        node.left = self.__delmin(node.left)
        node.n = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def print(self):
        self.__print(self.__root)
    
    def __print(self, node):
        if node == None:
            return
        self.__print(node.left)
        print(node.key, node.value)
        self.__print(node.right)