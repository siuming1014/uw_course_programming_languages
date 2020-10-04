# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # build a tuple which is [(v, w, v/w), ...]
    vw_tuple = [(values[i], weights[i], 1. * values[i] / weights[i]) for i in range(len(values))]
    # print(vw_tuple)
    vw_tuple.sort(key=lambda x: x[2], reverse=True)
    # print(vw_tuple)

    for v, w, v_over_w in vw_tuple:
        if w < capacity:
            value += v
            capacity -= w
        else:  # w >= capacity
            value += v_over_w * capacity
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
