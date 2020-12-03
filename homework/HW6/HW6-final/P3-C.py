# Problem 3-C -- Priority Queues -- for Homework 6 of CS107
# Extended by: Max Li

from P3 import timeit
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue

from matplotlib import pyplot as plt

ns = (10, 20, 50, 100, 200, 500)
naive_time = timeit(ns=ns, pqclass=NaivePriorityQueue)
myheap_time = timeit(ns=ns, pqclass=HeapPriorityQueue)
pythonheap_time = timeit(ns=ns, pqclass=PythonHeapPriorityQueue)

plt.plot(ns, naive_time, label="NaivePriorityQueue")
plt.plot(ns, myheap_time, label="HeapPriorityQueue")
plt.plot(ns, pythonheap_time, label="PythonHeapPriorityQueue")

plt.xlabel('Number of Lists Merged')
plt.ylabel('Elapsed time in seconds')
plt.title('Elapsed time with number of lists merged')
plt.legend()
plt.show()
