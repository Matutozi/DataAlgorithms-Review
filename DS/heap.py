"""IMPLEMENT HEAP"""

#Olog(n)

class MinHeap:
    def __init__(self):
        self.heap = []

    def peek(self):
        # return self.heap[0] or None
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        while 2 * i + 1 < len(self.heap):          
            left_child = 2 * i + 1                  
            right_child = 2 * i + 2
            
            smaller = left_child                   
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[left_child]:
                smaller = right_child
            
            if self.heap[i] > self.heap[smaller]:
                self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]
                i = smaller                        
            else:
                break