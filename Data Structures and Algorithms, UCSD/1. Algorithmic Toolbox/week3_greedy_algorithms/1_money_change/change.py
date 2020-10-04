# Uses python3
import sys

def get_change(m):
    #write your code here
    num = 0
    coins = (10, 5, 1)
    for coin in coins:
        num += m // coin
        m = m % coin
        if m is 0:
            break
    return num

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    #
    # print(get_change(2))
    # print(get_change(28))
