"""
File: test_asym_trie.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

import random
from trie import *

def create_str(length, p):
    """
    NatNum * Float -> String
    returns a binary string of length n where each digit has
    probability p of being a '1' 
    """
    st = ""
    for _ in range(0, length):
        r = random.random()
        if r < p:
            st += "1"
        else:
            st += "0"
    return st

def test():
    """
    test the trie functions on a large asymmetric trie
    """
    print("test asymmetric trie")
    
    random.seed(0)
    length = 64
    p = 0.75
    y = create_str(length, p)
    lst = [y]
    trie = Trie(None, y, None)
    
    print("test insert()")
    str_num = 100000
    for _ in range(1, str_num):
        x = create_str(length, p)
        lst.append(x)
        # Warning: this prints 100K False lines if insert is broken
        if not insert(trie, x):
            print(False)
    print(insert(trie, y) == False)

    
    print("test trie_to_list()")
    lst.sort()
    print(lst == trie_to_list(trie))
     
    print("test smallest()")
    print(lst[0] == smallest(trie))

    print("test largest()")
    print(lst[str_num-1] == largest(trie))

    print("test search()")
    x= create_str(length, p)
    print("0110111011111110011110011101110110111111011101011111110011110111" \
          == search(trie, x))
    x= create_str(length, p)
    print("0111111111101101111101111010111101111111111111101011010100111110" \
          == search(trie, x))
    x= create_str(length, p)
    print("0110001111111111110001111011111111100111010110100011000101101101" \
          == search(trie, x))

    print("test height()")   
    print(55 == height(trie))

    print("test size()")   
    print(str_num == size(trie))

# run the test
test()
