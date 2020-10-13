# python3
import sys

def InverseBWT(bwt):
    # write your code here
    first_col = sorted(bwt)

    _map = dict()
    last_col_idx = []
    for c in bwt:
        _map[c] = 1 if c not in _map else _map[c] + 1
        last_col_idx.append((c, _map[c]))

    _map = dict()
    first_col_idx_map = dict()
    for i, c in enumerate(first_col):
        _map[c] = 1 if c not in _map else _map[c] + 1
        first_col_idx_map[(c, _map[c])] = i

    ret_symbols = []
    cur_sym_of_first_col = ('$', 1)
    for _ in range(len(bwt)):
        cur_sym_of_last_col = last_col_idx[first_col_idx_map[cur_sym_of_first_col]]
        ret_symbols.append(cur_sym_of_last_col[0])
        cur_sym_of_first_col = cur_sym_of_last_col

    return "".join(reversed(ret_symbols))[1:] + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))