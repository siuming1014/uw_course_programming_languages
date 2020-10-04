# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def _recurInOrder(_i):
            if _i == -1:
                return
            _recurInOrder(self.left[_i])
            self.result.append(self.key[_i])
            _recurInOrder(self.right[_i])

        _recurInOrder(0)

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def _recurPreOrder(_i):
            if _i == -1:
                return
            self.result.append(self.key[_i])
            _recurPreOrder(self.left[_i])
            _recurPreOrder(self.right[_i])

        _recurPreOrder(0)

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        def _recurPostOrder(_i):
            if _i == -1:
                return
            _recurPostOrder(self.left[_i])
            _recurPostOrder(self.right[_i])
            self.result.append(self.key[_i])

        _recurPostOrder(0)

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
