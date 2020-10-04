# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):

    fibs_last_digit = [0, 1]

    for i in range(2, n + 1):
        # print(i)
        fibs_last_digit.append((fibs_last_digit[i - 1] + fibs_last_digit[i - 2]) % 10)

    return fibs_last_digit[n]


def calc_fib_memorized(n):

    fibs = [0, 1]

    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[n]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
    # print(get_fibonacci_last_digit_naive(n))
    # print(calc_fib_memorized(n))
