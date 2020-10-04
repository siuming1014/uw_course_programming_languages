# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a, b):
    # make a >= b
    if a < b:
        a, b = b, a

    # print(a, b)

    if b == 0:
        return a

    return gcd_fast(b, a % b)


def lcm_fast(a, b):

    d = gcd_fast(a, b)

    return int(a / d) * b


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    # print(a)
    # print(b)
    print(lcm_fast(a, b))
