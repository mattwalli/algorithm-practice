class HashTable:

    def __init__(self, size):
        self.size = size
        self.n = 0
        self.key_table = [None] * size
        self.value_table = [None] * size
    
    def put(self, key, value, resize = True):
        hash_key = hash(key) % self.size
        while True:
            if self.key_table[hash_key] == None:
                self.key_table[hash_key] = key
                self.n += 1
            if self.key_table[hash_key] == key:
                self.value_table[hash_key] = value
                break
            hash_key = (hash_key + 1) % self.size
        # Resize
        if self.n * 2 >= self.size and resize:
            self.resize(self.size * 2)
    
    def get(self, key):
        hash_key = hash(key) % self.size
        while True:
            if self.key_table[hash_key] == None:
                return None
            if self.key_table[hash_key] == key:
                return self.value_table[hash_key]
            hash_key = (hash_key + 1) % self.size

    def __len__(self):
        return self.n
    
    def delete(self, key):
        hash_key = hash(key) % self.size
        while True:
            if self.key_table[hash_key] == None:
                return
            if self.key_table[hash_key] == key:
                self.key_table[hash_key] = None
                self.value_table[hash_key] = None
                self.n -= 1
                # Following keys cant be probed to, replace in table
                while True:
                    self.hash_key = (hash_key + 1) % self.size
                    if self.key_table[hash_key] == None:
                        break
                    key, value = self.key_table[hash_key], self.value_table[hash_key]
                    self.key_table[hash_key], self.value_table[hash_key] = None, None
                    self.put(key, value)
                break
            hash_key = (hash_key + 1) % self.size
        # Resize
        if self.n * 8 < self.size:
            self.resize(self.size // 2)
    
    def resize(self, new_size):
        print(new_size)
        old_key_table = self.key_table.copy()
        old_value_table = self.value_table.copy()
        self.key_table = [None] * new_size
        self.value_table = [None] * new_size
        old_size = self.size
        self.size = new_size
        self.n = 0
        for i in range(old_size):
            if old_key_table[i] == None:
                continue
            self.put(old_key_table[i], old_value_table[i], False)


ht = HashTable(4)
ht.put("art", 1)
ht.put("ars", 1)
ht.put("ar", 1)
ht.put("arh", 1)
ht.put("ag", 1)
print(ht.key_table)
print(ht.value_table)