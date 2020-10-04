# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]
    import math
    n = len(self._data)
    for i in range(math.floor(n / 2), 0, -1):
      self.siftDown(i)
    # print(self._data)

  def siftDown(self, i):
    # print('i,', i)
    size = len(self._data)
    minIdx = i
    l = self.leftChild(i)
    r = self.rightChild(i)
    # print(i, l, r)
    # print(self._data[i - 1], self._data[l - 1], self._data[r - 1])
    if l <= size and self._data[l - 1] < self._data[minIdx - 1]:
      minIdx = l
    if r <= size and self._data[r - 1] < self._data[minIdx - 1]:
      minIdx = r
    # print(minIdx)
    if i != minIdx:
      self._swaps.append((i - 1, minIdx - 1))
      self._data[i - 1], self._data[minIdx - 1] = self._data[minIdx - 1], self._data[i - 1]
      self.siftDown(minIdx)

  def leftChild(self, i):
    return 2 * i

  def rightChild(self, i):
    return 2 * i + 1

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
