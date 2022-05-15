
# an almost full tree:
# in every sub tree, the root is the maximum namber
import numpy as np
import copy

class MaxHeap:
    def __init__(self):
        self.heap = [0, ]
        self.heap_size = 0
        self.MAX = 1

    def get_max(self):
        return self.heap[1]

    def parent(self, i):
        # get the parent index of i
        return i // 2

    def left(self, i):
        # return left child
        return 2 * i

    def right(self, i):
        # return left child
        return 2 * i + 1

    def max_heapify(self, i):
        # takes the i'th index of the heap and makes sure it follows the heap's rule:
        # a parent is larger then it's both children
        L = self.left(i)
        R = self.right(i)
        largest = i  # eventually points to the highest index of the three nodes
        if L <= self.heap_size and self.heap[L] > self.heap[i]:
            # if it's not a leaf and the left leaf is bigger the i
            largest = L
        if R <= self.heap_size and self.heap[R] > self.heap[largest]:
            # if it's not a leaf and the right leaf is bigger the largest => bigger then parent and left leaf
            largest = R
        if largest != i:  # one of i'th children is bigger then i
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # swap with larger child
            self.max_heapify(largest)  # largest still points to the

    def build_heap(self, A):
        self.heap_size = len(A)
        self.heap = copy.deepcopy(A)
        self.heap.insert(0,0)
        for i in range(self.heap_size // 2, 0, -1):
            self.max_heapify(i)

    def increase_key(self, i, k):
        if self.heap[i] >= k:
            return
        self.heap[i] = k
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]: # if bigger then parrent and not at the top
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)] # switch
            i = self.parent(i)  # change i to it's parent index

    def heap_insert(self, k):
        self.heap_size += 1
        self.heap.append(-np.inf)
        self.increase_key(self.heap_size, k)

    def extract_max(self):
        if self.heap_size < 1:
            return
        max = self.heap[self.MAX] # get max
        self.heap[self.MAX] = self.heap[self.heap_size] # put last as first
        del self.heap[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(self.MAX)
        return max

    @staticmethod
    def heap_sort(A):
        A = list(A)
        H2 = MaxHeap()
        H2.build_heap(A)
        A2 = []
        for i in range(len(A)):
            A2.append(H2.extract_max())
        return A2




