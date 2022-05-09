""" linked_list.py

Student: Jonathan Berntsson
Mail: Jokten123@gmail.com
Reviewed by: Kieran
Date reviewed: 06-05 -22
"""



class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ
        
        def to_list(self):
            if self.succ == None:
                return [self.data]
            else:
                return [self.data] + self.succ.to_list()
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        cur = self.first
        if cur is None:
            return 0
        len = 0
        while cur is not None:
            cur = cur.succ
            len += 1
        return len
  
  
    def mean(self):               # Optional
        len = 0
        cur = self.first
        sum = 0
        while cur is not None:
            sum += cur.data
            len += 1
            cur = cur.succ
        return sum/len
    
    
    def remove_last(self):        # Optional
        if self.first is None:
            return False
        if self.first.succ is None:
            return self.first.data
        cur = self.first
        while cur.succ.succ is not None:
            cur = cur.succ
        dat = cur.succ.data
        cur.succ = None
        return dat
    
    
    def remove(self, x):          # Compulsory
        if self.first == None:
            return False
        cur = self.first
        if cur.data == x:
            self.first = cur.succ
            return True

        while cur.succ is not None:
            if cur.succ.data == x:
                cur.succ = cur.succ.succ
                return True
            cur = cur.succ
        return False
            
    
    
    def count(self, x):           # Optional
        return self._count(x, self.first)

    def _count(self, x, f):
        if f == None:
            return 0
        else:
            return (f.data == x) + self._count(x,f.succ)
    
    
    def to_list(self):            # Compulsory
        if self.first == None:
            return []
        return self.first.to_list()
    
    
    def remove_all(self, x):      # Compulsory
        self.first = self._remove_all(x, self.first)
    
    def _remove_all(self, x, f):
        if f is None:
            return None
        elif f.data == x:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x, f.succ)
            return f

    
    
    def __str__(self):            # Compulsary
        string = ''
        for i in self:
            string += str(i) + ', '
        return '(' + string[:-2] + ')'
        
    
    
    def merge(self, lst):         # Compulsory
        for i in lst:
            self.insert(i)
            # N^2
    
    
    def __getitem__(self, ind):   # Compulsory
        for i in self:
            if ind == 0:
                return i
            else: 
                ind -= 1


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __lt__(self, other):
        return self.pnr < other.pnr

    def __eq__(self, other):
        return self.pnr == other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr

    def __gt__(self, other):
        return self.pnr > other.pnr
    
    def __ge__(self, other):
        return self.pnr >= other.pnr
    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    print(lst.length())
    print(lst.remove(3))
    print(lst.remove(3))
    print(lst.remove(7))
    lst.print()
    t = Person('Peter',123)
    p = Person('Eva',123)
    print(t==p)
    # Test code:

    


if __name__ == '__main__':
    main()
    


    

