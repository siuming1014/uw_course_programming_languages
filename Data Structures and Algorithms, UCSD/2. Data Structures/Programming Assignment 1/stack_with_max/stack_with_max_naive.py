#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []

    def Push(self, a):
        self.__stack.append(a)
        if not len(self.__max):
            self.__max.append(a)
        else:
            if a >= self.__max[-1]:
                self.__max.append(a)

    def Pop(self):
        assert(len(self.__stack))
        a = self.__stack.pop()
        if a == self.__max[-1]:
            self.__max.pop()

    def Max(self):
        assert(len(self.__max))
        return self.__max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
