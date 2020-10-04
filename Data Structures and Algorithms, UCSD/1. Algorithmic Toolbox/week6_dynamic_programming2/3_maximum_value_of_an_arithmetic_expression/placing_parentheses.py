# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    symbols = [dataset[i] for i in range(1, len(dataset), 2)]

    n = len(digits)
    m = [[None] * n for _ in range(n)]
    M = [[None] * n for _ in range(n)]

    def minAndMax(i, j):
        lst = sum([[evalt(M[i][k], M[k + 1][j], symbols[k]),
                    evalt(M[i][k], m[k + 1][j], symbols[k]),
                    evalt(m[i][k], M[k + 1][j], symbols[k]),
                    evalt(m[i][k], m[k + 1][j], symbols[k])] for k in range(i, j)], [])
        return min(lst), max(lst)

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = minAndMax(i, j)

    # print(M)
    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
    # print(get_maximum_value('5-8+7*4-8+9'))
