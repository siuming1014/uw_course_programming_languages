# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = (1, 3, 4)
    changes = []
    for i in range(m + 1):
        _coins = tuple(_ for _ in coins if _ <= i)
        if i == 0:
            _n = 0
        else:
            _n = min(changes[i - _coin] + 1 for _coin in _coins)
        changes.append(_n)
    return changes[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
