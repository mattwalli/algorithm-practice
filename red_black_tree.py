import random

class RBTree:
    class Node:
        RED = True
        BLACK = False
        def __init__(self, key, value, color):
            self.key = key
            self.value = value
            self.color = color
            self.left = None
            self.right = None
        
        def __str__(self):
            if self.color:
                return f"(RED:{self.key:03})"
            return f"(BLK:{self.key:03})"
    
    def __init__(self):
        self.root = None
    
    def __str__(self):
        display = self.__build_str("", self.root, -1, "=")
        return display
    
    def __build_str(self, disp, node, deep, pre):
        if node == None:
            return disp
        if self.is_red(node):
            pre = "|"
        else:
            deep += 1
        disp = self. __build_str(disp, node.right, deep, "/")
        for i in range(deep):
            disp += "          "
        disp += pre + str(node) + "\n"
        disp = self. __build_str(disp, node.left, deep, "\\")
        return disp

    def is_red(self, node):
        if node == None:
            return False
        return node.color == self.Node.RED
    
    def rotate_left(self, node):
        node_x = node.right
        node.right = node_x.left
        node_x.left = node
        node_x.color = node.color
        node.color = self.Node.RED
        return node_x
    
    def rotate_right(self, node):
        node_x = node.left
        node.left = node_x.right
        node_x.right = node
        node_x.color = node.color
        node.color = self.Node.RED
        return node_x
    
    def flip_colors(self, node):
        node.color = self.Node.RED
        node.left.color = self.Node.BLACK
        node.right.color = self.Node.BLACK
    
    def put(self, key, value):
        self.root = self.__put(self.root, key, value)
        self.root.color = self.Node.BLACK
    
    def __put(self, node, key, value):
        # Insert node here
        if node == None:
            return self.Node(key, value, self.Node.RED)
        # Go lower in tree
        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif node.key < key:
            node.right = self.__put(node.right, key, value)
        # Update value here
        else:
            node.value = value
        # Fix red links
        if self.is_red(node.right) and (not self.is_red(node.left)):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        return node
    
    def get(self, key):
        return self.__get(self.root, key)
    
    def __get(self, node, key):
        if node == None:
            return None
        if key < node.key:
            return self.__get(node.left, key)
        if node.key < key:
            return self.__get(node.right, key)
        return node.value

tree = RBTree()
for i in range(20):
    tree.put(random.randint(0,999), i)
print(tree)