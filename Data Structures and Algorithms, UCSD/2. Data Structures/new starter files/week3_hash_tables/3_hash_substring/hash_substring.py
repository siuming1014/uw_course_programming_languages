# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    prime = 1000000007
    multiplier = 263

    def are_equal(s, t):
        return s == t

    def hash_func(s, _prime=prime, _multiplier=multiplier):
        ans = 0
        for c in reversed(s):
            ans = (ans * _multiplier + ord(c)) % _prime
        return ans

    def precompute_hashes(T, len_P, p, x):
        len_T = len(T)
        ord_T = [ord(_) for _ in T]

        y = 1
        for _ in range(len_P):
            y = (y * x) % p

        H = [hash_func(T[len_T - len_P:len_T])]

        for i in range(len_T - len_P - 1, -1, -1):
            H.append((x * H[-1] + ord_T[i] - y * ord_T[i + len_P]) % p)

        H.reverse()
        return H

    len_pattern = len(pattern)
    len_text = len(text)

    p_hash = hash_func(pattern)

    hashes = precompute_hashes(text, len_pattern, prime, multiplier)

    # print(p_hash)
    # print(hashes)

    return [i for i in range(len_text - len_pattern + 1) if (p_hash == hashes[i]) and (are_equal(text[i:i + len_pattern], pattern))]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

