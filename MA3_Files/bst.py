""" bst.py

Student: Jonathan Berntsson
Mail: Jokten123@gmail.com
Reviewed by: Kieran
Date reviewed: 06-05 -22
"""

import random
import math
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)
    
    def _height(self, f):
        if f is None:
            return 0
        else:
            return 1 + max(self._height(f.right),self._height(f.left)) 

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right,k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                if r.right.left is None:
                    r.key = r.right.key
                    r.right = r.right.right
                else:
                    r.key = self._get_smallest(r.right)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def _get_smallest(self,r):
        if r.left.left == None:
            small = r.left.key
            r.left = None
            return small
        else:
            return self._get_smallest(r.left)

    def __str__(self):                            # Compulsory
        string = ''
        for i in self:
            string += str(i) + ', '
        return '<' + string[:-2] + '>'

    def to_list(self):                            # Compulsory
        list = []
        for i in self:
            list.append(i)
        return list

    def to_LinkedList(self):                      # Compulsory
        list = LinkedList()
        for i in self:
            list.insert(i)
        return list

    def ipl(self):                                # Compulsory
        return self._ipl(self.root, 1)
    
    def _ipl(self,r,depth):
        if r is None:
            return 0
        else:
            return self._ipl(r.right, depth+1) + depth + self._ipl(r.left, depth+1)



def random_tree(n):                               # Useful
    tree = BST()
    random.seed(1)
    for i in range(n):
        tree.insert(random.random())
    return tree



def main():
    """""
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9, 3]:
        print(f"contains({k}): {t.contains(k)}")
    """""
    res = []
    hei = []
    for i in [10, 20, 40, 80, 160, 320, 640]:
        t = random_tree(i*10)
        res.append(2**((t.ipl()/(i*10))/1.39))
        hei.append(t.height())
    print(res)
    print(hei)

if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? yes
2. computing height?
3. contains? yes
4. insert?
5. remove?




Results for ipl of random trees
===============================

[44.250624150161855, 96.57147312762456, 184.6663227392402, 394.3140861676359, 763.2380089951562, 1472.5039159458534, 2921.012259506185]
[13, 15, 18, 21, 25, 27, 30]




"""
