# Uses python3
def edit_distance(s, t):
    #write your code here
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

    return D[len_s][len_t]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
