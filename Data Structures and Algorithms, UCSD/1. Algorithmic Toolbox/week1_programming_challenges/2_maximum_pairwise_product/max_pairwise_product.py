# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):

    index_1 = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[index_1]:
            index_1 = i

    if index_1 is 0:
        index_2 = 1
    else:
        index_2 = 0

    for i in range(len(numbers)):
        if numbers[i] > numbers[index_2] and numbers[i] is not numbers[index_1]:
            index_2 = i

    return numbers[index_1] * numbers[index_2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
