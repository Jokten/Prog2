## Dictionary ADT ##
## Implemented with BS Tree
"""
Collection of key-value pair records, implemented as a binary search tree.
"""
# Name of class MUST be Dictionary
class Dictionary:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value
            
        def insert(self, key, value):
            if self.getKey() > key:
                if self.left is None:
                    self.left = Dictionary.Node(key, value)
                else:
                    self.left.insert(key, value)
            if self.getKey() < key:
                if self.right is None:
                    self.right = Dictionary.Node(key, value)
                else:
                    self.right.insert(key, value)

        def get(self, key):
            if self.getKey() == key:
                return self.getValue()
            elif self.getKey() < key:
                if self.right is None:
                    return None
                else:
                    print(f'Typ: {str(self.right)}')
                    return self.right.get(key)
            elif self.getKey() > key:
                if self.left is None:
                    return None
                return self.left.get(key)

        def delete(self, key):
            if key > self.getKey():
                if self.right is None:
                    return False
                elif self.right.getKey() == key:
                    self.right = self.right.__delete()
                    return True
                else:
                    return self.right.delete(key)
            elif key < self.getKey():
                if self.left is None:
                    return False
                elif self.left.getKey() == key:
                    self.left = self.left.__delete()
                    return True
                else:
                    return self.left.delete(key)



        def __iter__(self): #Should iterats over the Nodes in the tree
            yield self.getKey(), self.getValue()
            if self.right is not None:
                yield from self.right
            if self.left is not None:
                yield from self.left
        
        def __str__(self):
            return f'({self.getKey()}:{self.getValue()})'
        
        def __delete(self):      # Help method for delete (optional)
            if self.right is None and self.left is None:
                return None
            elif self.right is None and self.left is not None:
                return self.left
            elif self.right is not None and self.left is None:
                return self.right
            else:
                self.key, self.value = self.__getSmallest()
                return self

        def __getSmallest(self):      # Method used by __delete (optional)
            if self.left.left is None:
                key = self.left.getKey()
                value = self.left.getValue()
                self.left = None
                return key, value
            else:
                return self.left.__getSmallest()

        def deletefirst(self):
            return self.__delete()
        
# Dictionary methods start here:
    def __init__(self):
        self.__tree = None
        self.keys = set()

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """
    def insert(self, key, value):
        if key in self.keys:
            return False
        elif self.__tree is None:
            self.__tree = self.Node(key, value)
            self.keys.add(key)
            return True
        else:
            self.__tree.insert(key, value)
            self.keys.add(key)
            return True


    """
    Returns value that is identified by `key`, or None if no such key exists.
    """
    def get(self, key):
        if self.__tree is None:
            return None
        return self.__tree.get(key)

    """
    Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
    """
    def delete(self, key):
        if self.__tree is None:
            return False
        if self.__tree.getKey() == key:
            self.__tree = self.__tree.deletefirst()
            return True
            self.keys.remove(key)
        else:
            if self.__tree.delete(key):
                self.keys.remove(key)
                return True


    
    """
        Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
    """
    def __iter__(self):
        yield from self.__tree
    
    """ Returns a string representation of the key, values in the tree in order after key value (smallest to largest)
    """
    def __str__(self):
        st = ''
        for i in self:
            st += str(i)
        return st

