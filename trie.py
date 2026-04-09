class MinHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty MinHeap')
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        if self.data:
            self._heapify_down(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty MinHeap')
        return self.data[0]

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _heapify_up(self, i):
        while i > 0:
            parent_i = self._parent(i)
            if self.data[i] < self.data[parent_i]:
                self._swap(i, parent_i)
                i = parent_i
            else:
                break

    def _heapify_down(self, i):
        size = len(self.data)
        while True:
            left_i = self._left(i)
            right_i = self._right(i)
            smallest = i

            if left_i < size and self.data[left_i] < self.data[smallest]:
                smallest = left_i
            if right_i < size and self.data[right_i] < self.data[smallest]:
                smallest = right_i

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break


class MaxHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty MaxHeap')
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        if self.data:
            self._heapify_down(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty MaxHeap')
        return self.data[0]

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _heapify_up(self, i):
        while i > 0:
            parent_i = self._parent(i)
            if self.data[i] > self.data[parent_i]:
                self._swap(i, parent_i)
                i = parent_i
            else:
                break

    def _heapify_down(self, i):
        size = len(self.data)
        while True:
            left_i = self._left(i)
            right_i = self._right(i)
            largest = i

            if left_i < size and self.data[left_i] > self.data[largest]:
                largest = left_i
            if right_i < size and self.data[right_i] > self.data[largest]:
                largest = right_i

            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break
