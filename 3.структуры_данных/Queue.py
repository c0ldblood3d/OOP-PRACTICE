class Queue:
    def __init__(self, immutable_dequeue=False):
        self._line = []                 
        self._immutable = immutable_dequeue

    def enqueue(self, item):
        self._line.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        if self._immutable:
            return self._line[0]         
        else:
            return self._line.pop(0)    

    def is_empty(self):
        return len(self._line) == 0