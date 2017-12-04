from rit_lib import *

Trie = struct_type("Trie",
                   (("Trie", NoneType), "left"),
                   (object, "value"),
                   (("Trie", NoneType), "right"))

def insert(T, x):
    if real_insert(T, x, x):
        return True
    else:
        return False


def build_subtree(l, s, pre):
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
    if T.value == s:
        return False
    elif T.left is None and T.right is None and T.value is None:
        T.value = s
        return True
    elif T.value is not None:
        n = build_subtree(T.value, s, "")
        T.value = None
        T.left = n.left
        T.right = n.right
        return True
    elif x[0] == "0":
        if T.left is not None:
            return real_insert(T.left, x[1:], s)
        else:
            T.left = Trie(None, s, None)
    else:
        if T.right is not None:
            return real_insert(T.right, x[1:], s)
        else:
            T.right = Trie(None, s, None)


def trie_to_list(trie):
    lst = []
    data = trie_data_retrieval(trie)
    print(data)
    return data

def trie_data_retrieval(trie):
    if trie is None:
        return
    elif trie.value is not None:
        return trie.value
    elif trie.value is None:
        if trie.left is not None and trie.right is not None:
            return [trie_data_retrieval(trie.left), trie_data_retrieval(trie.right)]
        elif trie.right is None:
            return trie_data_retrieval(trie.left)
        elif trie.left is None:
            return trie_data_retrieval(trie.right)



def test_insert():
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
    print(trie_to_list(T))



test_list()