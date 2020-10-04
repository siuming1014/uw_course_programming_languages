#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if len(tree) == 0:
        return True
    keys = [_[0] for _ in tree]
    lefts = [_[1] for _ in tree]
    rights = [_[2] for _ in tree]
    checked_nodes = []

    def in_order_traversal(_i, is_right):
        # print(f'_i: {_i}, key: {keys[_i]}')
        if _i == -1:
            return
        if is_right:
            
        in_order_traversal(lefts[_i], False)
        if len(checked_nodes) == 0 or checked_nodes[-1] < keys[_i]:
            checked_nodes.append(keys[_i])
        else:
            return
        in_order_traversal(rights[_i], True)

    in_order_traversal(0, False)
    # print(checked_nodes)
    if len(checked_nodes) == len(tree):
        return True
    else:
        return False



def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
