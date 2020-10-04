# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


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


def fibonacci_sum_squares_fast(n):

    return (get_fibonacci_huge_fast(n, 10) * get_fibonacci_huge_fast(n + 1, 10)) % 10


if __name__ == '__main__':
    # n = int(stdin.read())
    n = int(input())
    # n = 1234567890
    print(fibonacci_sum_squares_fast(n))
