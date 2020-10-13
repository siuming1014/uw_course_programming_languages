# python3
import sys

def BWT(text):
    n = len(text)
    M = [text[n - i:] + text[:n - i] for i in range(n)]
    return "".join(s[-1] for s in sorted(M))

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
