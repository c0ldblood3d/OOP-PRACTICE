class _Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    def __init__(self, case_sensitive=True):
        self._top = None               
        self._size = 0                
        self._case_sensitive = case_sensitive

    def push(self, item):
        if isinstance(item, str) and not self._case_sensitive:
            item = item.lower()
        new_node = _Node(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return ""
        popped_value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return popped_value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size

    def peek(self):
        if self.is_empty():
            return ""
        return self._top.value