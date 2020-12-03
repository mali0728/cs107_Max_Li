# Problem 3-C -- Priority Queues -- for Homework 6 of CS107
# Extended by: Max Li

from random import sample
from time import time
import heapq

from P2 import MinHeap

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError  # TODO

    def get(self):
        raise NotImplementedError  # TODO

    def peek(self):
        raise NotImplementedError  # TODO


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end - start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):

    def __init__(self, max_size):
        super().__init__(max_size) 

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('The priority queue is already full')
        else:
            self.elements.append(val)

    def get(self):
        if len(self) == 0:
            raise IndexError('The priority queue is empty')

        minimum = min(self.elements)
        self.elements.remove(minimum)
        return minimum

    def peek(self):
        if len(self) == 0:
            raise IndexError('The priority queue is empty')

        minimum = min(self.elements)
        return minimum


class HeapPriorityQueue(PriorityQueue):
    
    def __init__(self, max_size):
        super().__init__(max_size) 
        self.heap = MinHeap(self.elements)

    def put(self, val):
        if len(self) >= self.max_size:
            raise IndexError('The priority queue is already full')

        self.heap.heappush(val)


    def get(self):
        if len(self) == 0:
            raise IndexError('The priority queue is empty')

        return self.heap.heappop()

    def peek(self):
        if len(self) == 0:
            raise IndexError('The priority queue is empty')

        return self.heap.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):

    def put(self, val):
        if len(self) >= self.max_size:
            raise IndexError('The priority queue is already full')
        heapq.heappush(self.elements, val)


    def get(self):
        if len(self) <= 0:
            raise IndexError('The priority queue is empty')
        return heapq.heappop(self.elements)

    def peek(self):
        if len(self) <= 0:
            raise IndexError('The priority queue is empty')
        return self.elements[0]

'''
if __name__ == "__main__":
    print("<<<<<<<<<<<<<<part A>>>>>>>>>>>>>>")
    q = NaivePriorityQueue(4)
    q.put(1)
    q.put(2)
    q.put(-1)
    q.put(-2)
    print(q.peek())
    print(q.elements)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.elements)
    print(q.get())
    #print(q.get()) # error
    print("<<<<<<<<<<<<<<part B>>>>>>>>>>>>>>")

    q = HeapPriorityQueue(5)
    q.put(4)
    q.put(2)
    q.put(3)
    q.put(1)
    print(q.peek())
    print(q.elements)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    #print(q.get()) # error
    print(q.elements)

    print("<<<<<<<<<<<<<<part C>>>>>>>>>>>>>>")
    q2 = PythonHeapPriorityQueue(5)
    q2.put(5)
    q2.put(3)
    q2.put(2)
    q2.put(20)
    print(q2.peek())
    print(q2.elements)
    print(q2.get())
    print(q2.get())
    print(q2.get())
    print(q2.get())
    '''