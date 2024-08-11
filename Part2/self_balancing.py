"""LEARNING ABOUR HASH TABLES
dictinary are implemented using hash tables"""

def get_index(data_list, key):
    #Generate an index for a key using a hash function
    hash_code = hash(key)
    index = hash_code % len(data_list)
    return index
#the above is the more acceptable version of getting the hash value

def get_index(data_list, key):
    index = 0
    for char in key:
        index += ord(char)
    return (index % len(data_list))

MAX_HASH_TABLE_SIZE = 4096
class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] *max_size

    def insert(self, key, value):
        """Method that inserts a new key value pair"""
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        """MEthod that finds a value given a key"""
        idx = get_index(self.data_list, key)

        kv= self.data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value
        

    def update(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
        
        
ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.find("apple"))
print(ht.list_all())


#CODE THAT TAKES CARE OF COLLISION
