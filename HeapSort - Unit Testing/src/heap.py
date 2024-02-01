class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]
