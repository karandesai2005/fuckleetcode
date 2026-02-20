from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(type(queue))
queue.popleft()
print(queue)

queue.appendleft(12)
print(queue)
queue.pop()
print(queue)
