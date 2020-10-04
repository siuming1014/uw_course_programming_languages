# Uses python3
import sys

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1

def get_majority_element(a, left, right):
    n = len(a)
    a.sort()
    current_element = a[0]
    i = 1
    for _a in a[1:]:
        # print('current_element', current_element)
        # print('i', i)
        if _a == current_element:
            i += 1
        else:
            if i > n / 2:
                return 1
            else:
                current_element = _a
                i = 1
    if i > n / 2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
