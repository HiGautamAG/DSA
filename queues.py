# Queues follow the first-in-first-out (FIFO) principle.


from collections import deque 

queue = deque()

queue.append(1)
queue.append(2)


print(queue.popleft())