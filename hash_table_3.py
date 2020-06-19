class HashTable:

    class Data:
        def __init__(self, key, value):
            self.key = key
            self.value = value
        
        def __str__(self):
            return f"({self.key}:{self.value})"

    def __init__(self, n):
        self.table = [[] for _ in range(n)]
        self.n = n
    
    def __str__(self):
        ret = ""
        for line in self.table:
            for data in line:
                ret += str(data)
            ret += "\n"
        return ret
    
    def put(self, key, value):
        hash_key = hash(key) % self.n
        new_data = self.Data(key, value)
        for old_data in self.table[hash_key]: # Existing sub list
            if old_data.key == new_data.key:
                old_data.value = new_data.value # Update value
                return
        # Empty sublist or list without target key
        self.table[hash_key].append(new_data)
        return
    
    def get(self, key):
        hash_key = hash(key) % self.n
        for data in self.table[hash_key]:
            if data.key == key:
                return data.value
        return None # Search miss

    def delete(self, key):
        hash_key = hash(key) % self.n
        for data in self.table[hash_key]:
            if data.key == key:
                self.table[hash_key].remove(data)