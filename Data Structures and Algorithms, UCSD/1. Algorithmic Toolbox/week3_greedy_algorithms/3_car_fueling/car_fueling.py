# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    last_refill_pos = 0
    current = 0
    num_refills = 0
    # print('stops', stops)

    nxt = stops.pop(0)
    while True:
        if nxt - last_refill_pos <= tank:
            # print(f'move from {current} to {next}')
            current = nxt
            if len(stops) is 0:
                break
            else:
                nxt = stops.pop(0)
        else:
            # print(f'not enough fuel to move from {current} to {next}')
            if last_refill_pos == current:
                # print('impossible')
                return -1
            elif last_refill_pos < current:
                num_refills += 1
                last_refill_pos = current
                # print(f'refill at {last_refill_pos}')

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
