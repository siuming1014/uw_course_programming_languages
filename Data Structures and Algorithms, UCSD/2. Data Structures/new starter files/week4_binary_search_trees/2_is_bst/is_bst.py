#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


# def IsBinarySearchTree(tree):
#     # Implement correct algorithm here
#     if len(tree) == 0:
#         return True
#     keys = [_[0] for _ in tree]
#     lefts = [_[1] for _ in tree]
#     rights = [_[2] for _ in tree]
#     checked_nodes = []
#
#     def in_order_traversal(_i):
#         # print(f'_i: {_i}, key: {keys[_i]}')
#         if _i == -1:
#             return
#         in_order_traversal(lefts[_i])
#         checked_nodes.append(keys[_i])
#         in_order_traversal(rights[_i])
#
#     in_order_traversal(0)
#     # print(checked_nodes)
#     for i in range(len(checked_nodes) - 1):
#         # print(i)
#         if checked_nodes[i] >= checked_nodes[i + 1]:
#             return False
#
#     return True


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if len(tree) == 0:
        return True
    keys = [_[0] for _ in tree]
    lefts = [_[1] for _ in tree]
    rights = [_[2] for _ in tree]
    checked_nodes = []

    def in_order_traversal(_i):
        # print(f'_i: {_i}, key: {keys[_i]}')
        if _i == -1:
            return
        in_order_traversal(lefts[_i])
        if len(checked_nodes) == 0 or checked_nodes[-1] < keys[_i]:
            checked_nodes.append(keys[_i])
        else:
            return
        in_order_traversal(rights[_i])

    in_order_traversal(0)
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


def test():
    with open('../1_tree_traversals/tests/21', 'r') as fh:
        tree = []
        for i, line in enumerate(fh):
            if i == 0:
                nodes = int(line.strip())
            else:
                tree.append(list(map(int, line.strip().split())))
        assert nodes == len(tree)
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")


threading.Thread(target=main).start()
