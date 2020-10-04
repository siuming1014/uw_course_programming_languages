# Uses python3
import sys

def optimal_sequence(n):
    sequences = [[1]]  # sequences[n-1] = a_n
    for i in range(2, n + 1):
        # print(i, sequences)
        prev_steps = [i - 1]
        if i % 2 == 0:
            prev_steps.append(i // 2)
        if i % 3 == 0:
            prev_steps.append(i // 3)
        prev_step_sequences = [sequences[_ - 1] for _ in prev_steps]
        # print('prev_step_sequences', prev_step_sequences)
        min_sequences = min(prev_step_sequences, key=len).copy()
        min_sequences.append(i)
        # print('min_sequences', min_sequences)
        sequences.append(min_sequences)
    # print(sequences)
    return sequences[n - 1]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
