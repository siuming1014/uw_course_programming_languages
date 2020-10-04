# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):

    m = 10

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

    if period is None:
        return sum(mods[:n + 1]) % m

    # n = a * period + b
    a = int(n / period)
    b = n % period

    return ((a + 1) * sum(mods[i] for i in range(0, b + 1)) + a * sum(mods[i] for i in range(b + 1, period))) % m


if __name__ == '__main__':
    # input = sys.stdin.read()
    input = input()
    # input = 832564823476
    n = int(input)
    print(fibonacci_sum_fast(n))
