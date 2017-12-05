from rit_lib import *

Trie = struct_type("Trie",
                   (("Trie", NoneType), "left"),
                   (object, "value"),
                   (("Trie", NoneType), "right"))


def insert(T, x):
    """
    having only 2 parameters was stupid, calls a good 3 parameter insert
    :param T: Trie type
    :param x: string to insert
    :return: True or false, depending on the success of the insert
    """
    if real_insert(T, x, x):
        return True
    else:
        return False


def build_subtree(l, s, pre):
    """
    builds subtree when a leaf is already present
    :param l: string found on the leaf
    :param s: original string to insert
    :param pre: prefix of both l and s, a precursor to finding this tree
    :return: Either false if they're the same value, or a new Trie that has l and s properly distinguished or something
    """
    if l == s:
        return False
    elif l[0] == s[0]:
        if l[0] == "0":
            return Trie(build_subtree(l[1:],s[1:], pre + l[0]), None, None)
        elif l[0] == "1":
            return Trie(None, None, build_subtree(l[1:], s[1:], pre + l[0]))
    else:
        if l[0] == "0":
            return Trie(Trie(None, pre + l, None), None, Trie(None, pre + s, None))
        else:
            return Trie(Trie(None, pre + s, None), None, Trie(None, pre + l, None))


def real_insert(T, x, s):
    """
    insert's cooler older brother, takes a trie, a string splice, and the original string
    :param T: Trie struct, can be empty, not empty, or fun, but not all at once
    :param x: substring of s, used to compare with further steps of the ladder
    :param s: whole string
    :return: either True if it is inserted, or False if the value is already in the Trie
    """
    if T.value == s:
        return False
    elif T.value is None and T.left is None and T.right is None:
        T.value = s
        return True
    elif T.value is not None:
        index = len(s) - len(x) # im sorry for this spaghetti, but it works so hey
        n = build_subtree(T.value[index:], x, s[0:len(s)-len(x)])
        T.value = None
        T.left = n.left
        T.right = n.right
        return True
    elif x[0] == "0":
        if T.left is None:
            T.left = Trie(None, s, None)
            return True
        else:
            return real_insert(T.left, x[1:], s)
    elif x[0] == "1":
        if T.right is None:
            T.right = Trie(None, s, None)
            return True
        else:
            return real_insert(T.right, x[1:], s)


def trie_to_list(trie):
    """
    ghetto a'f method of getting a trie to a list, where theres a cool string intermediary step.
    :param trie: Trie type
    :return: list of strings in order
    """
    data = trie_data_retrieval(trie)
    data = data.split(",")
    return data


def trie_data_retrieval(trie):
    """
    helper function of trie_to_list, recursively retrieves all of the data in order
    :param trie: Trie struct
    :return: string of all the data, separated by commas
    """
    if trie is None:
        return
    elif trie.value is not None:
        return trie.value
    elif trie.value is None:
        if trie.left is not None and trie.right is not None:
            return trie_data_retrieval(trie.left)+","+trie_data_retrieval(trie.right)
        elif trie.left is None:
            return trie_data_retrieval(trie.right)
        elif trie.right is None:
            return trie_data_retrieval(trie.left)


def largest(trie):
    """
    finds the largest string in the trie
    :param trie: Trie struct
    :return: largest string
    """
    if trie.left is None and trie.right is None:
        return trie.value
    elif trie.right is not None:
        return largest(trie.right)
    elif trie.right is None and trie.left is not None:
        return largest(trie.left)


def smallest(trie):
    """
    finds the smallest string in the Trie
    :param trie: Trie trype
    :return: smallest string
    """
    if trie.left is None and trie.right is None:
        return trie.value
    elif trie.left is not None:
        return smallest(trie.left)
    elif trie.left is None and trie.right is not None:
        return smallest(trie.right)


def search(trie, st):
    fuck_this = "I got other things to do"
    return fuck_this


def size(trie):
    if trie is None:
        return 0
    elif trie.value is not None:
        return 1
    elif trie.value is None:
        if trie.left is not None and trie.right is not None:
            return size(trie.left)+size(trie.right)
        elif trie.left is None:
            return size(trie.right)
        elif trie.right is None:
            return size(trie.left)


def height(trie):
    pass

def test_insert():
    """
    test function for insertion
    :return: none
    """
    T = Trie(None, None, None)
    print(insert(T, "00"))
    print(T)
    print(insert(T, "00"))
    print(T)
    print(insert(T, "11"))
    print(T)
    print(insert(T, "01"))
    print(T)
    print(insert(T, "01"))
    print(T)
    print(insert(T, "10"))
    print(T)
    list = trie_to_list()


def test_list():
    """
    test function for making and returning a list
    :return: None
    """
    T = Trie(None, None, None)
    insert(T, "0000")
    insert(T, "0001")
    insert(T, "0010")
    insert(T, "0011")
    insert(T, "0100")
    insert(T, "0101")
    insert(T, "0110")
    insert(T, "0111")
    insert(T, "1000")
    insert(T, "1001")
    insert(T, "1010")
    insert(T, "1011")
    insert(T, "1100")
    insert(T, "1101")
    insert(T, "1110")
    insert(T, "1111")
    print(T)
    print(trie_to_list(T))
    print(largest(T))
    print(smallest(T))
    print(size(T))


test_list()