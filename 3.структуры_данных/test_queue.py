from Queue import Queue

queue = Queue(immutable_dequeue = True)
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
print("Current Queue :" , queue._line)
print("Dequeued item :" , queue.dequeue()) 
print("Dequeued item :" , queue.dequeue()) 
print("Updated Queue :" , queue._line) 