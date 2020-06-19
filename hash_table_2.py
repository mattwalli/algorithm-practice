class HashTable:

    class LLNode:

        def __init__(self, key, next_ = None):
            self.key = key
            self.next = next_
        
    def __init__(self, n):
        self.table = [None] * n
        self.n = n

    def __str__(self):
        line = ""
        for i in range(len(self.table)):
            line += f"{i}- "
            node = self.table[i]
            while node != None:
                line += f"{node.key} "
                node = node.next
            line += "\n"
        return line
    
    def put(self, key):
        key_hash = hash(key) % self.n
        node = self.table[key_hash]
        while True:
            if node == None:
                self.table[key_hash] = self.LLNode(key, self.table[key_hash])
                return
            if node.key == key:
                return
            node = node.next

    def get(self, key):
        key_hash = hash(key) % self.n
        node = self.table[key_hash]
        while True:
            if node == None:
                return None
            if node.key == key:
                return key
            node = node.next
    
    def delete(self, key):
        key_hash = hash(key) % self.n
        if self.table[key_hash] != None:
            if self.table[key_hash].key == key: # in first node
                self.table[key_hash] = self.table[key_hash].next
            else:
                last_node = self.table[key_hash]
                this_node = last_node.next
                while this_node != None:
                    if this_node.key == key: # found it, delete
                        last_node.next = this_node.next
                        return
                    else:
                        last_node = this_node
                        this_node = this_node.next