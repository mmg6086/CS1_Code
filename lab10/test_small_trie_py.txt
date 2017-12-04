"""
File: test_small_trie.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

from trie import *

def test():
    """
    test trie functions on a small tree.
    """
    print("test small trie")
    
    X1 = "001010"
    X2 = "000111"
    X3 = "111000"
    X4 = "010000"
    X5 = "110001"

    trie = Trie(None, X1, None)
    print("test insert()")
    print(insert(trie, X2))
    print(insert(trie, X3))
    print(insert(trie, X4))
    print(insert(trie, X5)) 
    print(insert(trie, X3) == False)
    
    print("test trie_to_list()")
    print([X2, X1, X4, X5, X3] == trie_to_list(trie))
    print([X2, X1, X4] == trie_to_list(trie.left))
    print([X5, X3] == trie_to_list(trie.right))

    
    print("test smallest()")
    print(X2 == smallest(trie))
    print(X5 == smallest(trie.right))

    print("test largest()")
    print(X3 == largest(trie))
    print(X4 == largest(trie.left))

    print("test search()")
    print(X1 == search(trie, X1))
    print(X3 == search(trie, "111011"))
    print(X5 == search(trie, "101111"))
    print(X4 == search(trie, "011111"))

    print("test height()")
    print(0 == height(None))
    print(0 == height(Trie(None, X1, None)))
    print(3 == height(trie))
    
    print("test size()")
    print(0 == size(None))
    print(1 == size(Trie(None, X1, None)))
    print(5 == size(trie))

# run the test
test()
