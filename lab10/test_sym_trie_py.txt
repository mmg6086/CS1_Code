"""
File: test_sym_trie.py
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
    test functions on a large symmetric trie
    """
    print("test symmetric trie")
    
    random.seed(0)
    length = 48
    p = 0.5
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

    lst.sort()
    print("test trie_to_list()")
    print(lst == trie_to_list(trie))
    
    print("test smallest()")
    print(lst[0] == smallest(trie))

    print("test largest()")
    print(lst[str_num-1] == largest(trie))

    print("test search()")
    x= create_str(length, p)
    print("110011010000100101011111001011110110111111110100" == search(trie, x))
    x= create_str(length, p)
    print("010100001011110111101110101000110111110101101010" == search(trie, x))
    x= create_str(length, p)
    print("001000000110000001010010111100011011100000010110" == search(trie, x))

    print("test height()")   
    print(33 == height(trie))

    print("test size()") 
    print(str_num == size(trie))
test()
