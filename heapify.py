class Heapify:
    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        return repr(self.arr)

    def MaxChild(self, i, size):
        if (i * 2) + 2 > size:
            return (i * 2) + 1
        else:
            if self.arr[(i*2)+2] > self.arr[(i*2)+1]:
                return (i*2)+2
            else:
                return (i*2)+1

    def SiftDown(self, i, size): #with size parameter, you can limit the search to a certain amount of elements.
        while (i*2)+1 <= size:
            m = self.MaxChild(i, size)
            if self.arr[i] < self.arr[m]:
                self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
                i = m
            else:
                return

    def heapify(self):
        i = len(self.arr) - 1
        while i >= 0:
            self.SiftDown(i, len(self.arr)-1)
            i -= 1
        return self.arr

    def heapsort(self):
        i = 0
        adjust = len(self.arr)-1
        while adjust > 0:
            self.arr[0], self.arr[adjust] = self.arr[adjust], self.arr[0]
            adjust -= 1
            self.SiftDown(0, adjust)

array = [1, 12, 9, 5, 6, 10, 31]
heap = Heapify(array)
heap.heapify()
print(heap.arr)
heap.heapsort()
print(heap.arr)
