#Uses python3

import sys
import random

# def lcs2(a, b):
#     #write your code here
#     return min(len(a), len(b))


def lcs2(s, t):
    # write your code here
    len_s, len_t = len(s), len(t)
    D = [[None] * (len_t + 1) for _ in range(len_s + 1)]  # D[i][j] = D(i, j)
    for i in range(len_s + 1):
        for j in range(len_t + 1):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            else:
                D[i][j] = min(D[i][j - 1] + 1,
                              D[i - 1][j] + 1,
                              D[i - 1][j - 1] + int(s[i - 1] != t[j - 1]))

    # return D[len_s][len_t]
    lcs = []
    aligned_s = []
    aligned_t = []
    i = len_s
    j = len_t
    while (i > 0) and (j > 0):
        if D[i][j] == D[i - 1][j] + 1:
            aligned_s.append(s[i - 1])
            aligned_t.append('')
            i -= 1
        elif D[i][j] == D[i][j - 1] + 1:
            aligned_s.append('')
            aligned_t.append(t[j - 1])
            j -= 1
        else:
            if D[i][j] == D[i - 1][j - 1]:
                lcs.append(str(s[i - 1]))
                aligned_s.append(s[i - 1])
                aligned_t.append(t[j - 1])
            else:
                aligned_s.append(s[i - 1])
                aligned_t.append(t[j - 1])
            i -= 1
            j -= 1

    # print(D)
    lcs.reverse()
    aligned_s.reverse()
    aligned_t.reverse()
    print('aligned_s', aligned_s)
    print('aligned_t', aligned_t)
    print('lcs', lcs)
    return len(lcs)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    #
    # n = data[0]
    # data = data[1:]
    # a = data[:n]
    #
    # data = data[n:]
    # m = data[0]
    # data = data[1:]
    # b = data[:m]
    #
    # print(lcs2(a, b))

    for i in range(1):
        a = [random.choice(range(-1000000000, 1000000000)) for _ in range(random.choice(range(1, 101)))]
        b = [random.choice(range(-1000000000, 1000000000)) for _ in range(random.choice(range(1, 101)))]
        print('a', a)
        print('b', b)
        print(lcs2(a, b))
