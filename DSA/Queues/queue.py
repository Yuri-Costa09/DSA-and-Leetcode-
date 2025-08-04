from queue import Queue
from collections import deque

q = Queue()

# Follows the FIFO (FIRST IN, FIRST OUT).

# Adds an element at the end of the queue
q.put(1)
q.put(3)
q.put(6)
q.put(5)

# Removes the first element of the queue
print(q.get())

# Implementation of a queue
