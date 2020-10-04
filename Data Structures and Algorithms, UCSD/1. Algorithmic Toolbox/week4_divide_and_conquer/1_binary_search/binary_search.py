# Uses python3
import sys


def binary_search_recursive(a, x):
    # base case
    if len(a) is 0:
        return -1

    left, right = 0, len(a)
    middle = (left + right) // 2

    if x == a[middle]:
        return middle
    elif x < a[middle]:
        return binary_search_recursive(a[left:middle], x)
    else:
        nxt = binary_search_recursive(a[middle + 1:right], x)
        return middle + 1 + nxt if nxt >= 0 else -1


def binary_search(a, x):
    # base case
    if len(a) is 0:
        return -1

    left, right = 0, len(a)
    while left < right:
        middle = (left + right) // 2
        if x == a[middle]:
            return middle
        elif x < a[middle]:
            right = middle
        else:
            left = middle + 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
