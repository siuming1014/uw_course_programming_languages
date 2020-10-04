# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Tree:

    def __init__(self, n, parents):
        self.n = n
        self.parents = parents
        self.root = None
        self.childs = [[] for _ in range(self.n)]
        for i, _parent in enumerate(self.parents):
            if _parent == -1:
                self.root = i
            else:
                self.childs[_parent].append(i)
        # print(self.childs)

    @staticmethod
    def height(tree, root):
        # Replace this code with a faster implementation
        # print(root)
        return 1 + (0 if len(tree.childs[root]) is 0 else max(Tree.height(tree, _root) for _root in tree.childs[root]))


def main():
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    tree = Tree(n, parents)
    print(tree.height(tree, tree.root))


# def test():
#     for i in range(1, 25):
#         file_name = f'0{i}' if i < 10 else str(i)
#         with open(f'./tests/{file_name}', 'r') as fh:
#             lines = [_[:-1] for _ in fh]
#             # print(lines)
#             n = int(lines[0])
#             parents = list(map(int, lines[1].split()))
#             tree = Tree(n, parents)
#             print(tree.height(tree, tree.root))


threading.Thread(target=main).start()
