import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
    print(q.get(), end="->")

print()

pq = queue.PriorityQueue()

pq.put([2, 'a'])
pq.put([1, 'b'])
pq.put([3, 'e'])

while not pq.empty():
    print(pq.get(), end="->")
