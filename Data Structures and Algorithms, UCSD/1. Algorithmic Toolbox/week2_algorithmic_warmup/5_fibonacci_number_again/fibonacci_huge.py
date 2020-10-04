# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    fibs = [0, 1]
    mods = [0, 1]
    period = None

    for i in range(2, n + 1):
        # print('i', i)
        fibs.append(fibs[i - 1] + fibs[i - 2])
        mods.append(fibs[i] % m)

        if mods[i - 1] is 0 and mods[i] is 1:
            period = i + 1 - 2
            break

    # print(period)

    if period is None:
        return fibs[n] % m
    else:
        return fibs[n % period] % m


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
    # print(get_fibonacci_huge_naive(n, m))
