"""
Collection of key-value pair records, implemented as a linked list.
"""
# Name of class MUST be Dictionary
class Dictionary:
    
    """
    Represents a single item within the linked list.
    """
    class Node:
        # Initialize dictionary
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.nextNode = None
            
        def getKey(self):
            return self.key

        def getValue(self):
            return self.value
            
        def insert(self, key, value):
            if (self.nextNode is None or self.nextNode.getKey() > key) and self.getKey() < key:
                old = self.nextNode
                self.nextNode = Dictionary.Node(key, value)
                self.nextNode.nextNode = old
                print(f'Inserted {key}:{value}')
            else:
                self.nextNode.insert(key, value)
        def get(self, key):
            print(f'Getter {key}')
            print(f'My key {self.key}')
            if self.key == key:
                print(f'Returned {self.value}')
                return self.value
            elif self.nextNode is None:
                return None
            else:
                return self.nextNode.get(key)

        def delete(self, key):
            if self.nextNode is None:
                return False
            elif self.nextNode.getKey() == key:
                print(f'GG {self.nextNode.nextNode}')
                print(f'Deleting {self.nextNode}')
                old = self.nextNode
                self.nextNode = old.nextNode
                print(f'New next {self.nextNode}')

                return True
            else:
                return self.nextNode.delete(key)

        def __iter__(self): #Should iterats over the Nodes in the list
            next = self
            while next is not None:
                yield next.getKey(), next.getValue()
                next = next.nextNode

        def __str__(self):
            return f'({self.getKey()}:{self.getValue()})'
        
    # Dictionary methodes start here:
    def __init__(self):
        self.__head = None
        self.key_val = set()
        self.key_set = set()

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """
    def insert(self, key, value):
        print(f'Trying {key, value}')
        if key in self.key_val:
            return False

        elif self.__head is None:
            self.__head = self.Node(key, value)
            self.key_val.add(key)
            print(f'Inserted {key}:{value}')
            return True
        elif self.__head.getKey() > key:
            new_head = Dictionary.Node(key, value)
            new_head.nextNode = self.__head
            self.__head = new_head
        else:
            self.__head.insert(key, value)
            self.key_val.add(key)
            return True

    """
    Returns value that is identified by `key`, or None if no such key exists.
    """
    def get(self, key):
        if self.__head is None:
            return None
        else:
            return self.__head.get(key)

    """
    Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
    """
    def delete(self, key):
        if self.__head.getKey() == key:
            self.__head = self.__head.nextNode
        else:
            print(f'Deleted {key}')
            return self.__head.delete(key)
    
    """
        Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
    """
    def __iter__(self):
        yield from self.__head
    
    
    """ Returns a string representation of the key, values in the linked list from the start to the end (sorted).
    """
    def __str__(self):
        st = ''
        for i in self.__head:
            st += str(i)
        return st




