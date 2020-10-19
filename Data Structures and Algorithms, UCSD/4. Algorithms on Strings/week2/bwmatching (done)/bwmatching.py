# python3
import sys
from typing import Dict, AnyStr, List


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  starts: Dict[string, int] = dict()
  occ_counts_before: Dict[string, List[int]] = {c: [] for c in bwt}

  for i, c in enumerate(sorted(bwt)):
    if c not in starts:
      starts[c] = i
  
  occ_counts_before = {c: [0] for c in bwt}
  for c in bwt:
    for c2 in occ_counts_before:
      occ_counts_before[c2].append(occ_counts_before[c2][-1] + (1 if c == c2 else 0))

  return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  # from pprint import pprint
  # pprint(starts)
  # pprint(occ_counts_before)

  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if len(pattern):
      symbol = pattern[-1]
      pattern = pattern[:-1]
      if symbol in starts:
        top = starts[symbol] + occ_counts_before[symbol][top]
        bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
      else:
        return 0
    else:
      return bottom - top + 1
  return 0
     
if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
