# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) is 0:
                return i + 1
            _, left = opening_brackets_stack.pop(-1)
            if not are_matching(left, next):
                return i + 1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[-1][0] + 1
    else:
        return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch if mismatch else 'Success')


if __name__ == "__main__":
    main()
