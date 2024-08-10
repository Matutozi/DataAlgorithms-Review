"""AS a senior backend engineer, u are tasked with developing a fast data structure to mamange profile information for 100 million users.
insert: insert new profile info for new user
find: profile info of user given username
update: profile info given username
list: to list all users on plafform slrted by username
"""
from  bst_key_val_pair import find, update, insert, balanced_bst, list_all
class TreeMap:
    def __init__(self):
        self.root = None


    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balanced_bst(self.root)

        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else  None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    