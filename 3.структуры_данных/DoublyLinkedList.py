class Node:
    def __init__(self, item_value):
        self._content = item_value
        self._ptr_next = None
        self._ptr_prev = None


class DoublyLinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None

    def display(self):
        if self._head_node is None:
            print("пусто")
            return

        s = ""
        current = self._head_node
        while current:
            s += str(current._content)
            if current._ptr_next:
                s += "."
            current = current._ptr_next
        print(s)

    def _length(self):
        count = 0
        current = self._head_node
        while current:
            count += 1
            current = current._ptr_next
        return count

    def insert(self, value):
        new_node = Node(value)

        if self._head_node is None:
            self._head_node = self._tail_node = new_node
            return

        length = self._length()
        mid = length // 2
        current = self._head_node
        for _ in range(mid):
            current = current._ptr_next

        if length % 2 == 0:
            prev_node = current._ptr_prev
            if prev_node:
                prev_node._ptr_next = new_node
                new_node._ptr_prev = prev_node
            else:
                self._head_node = new_node
            new_node._ptr_next = current
            current._ptr_prev = new_node
        else:
            next_node = current._ptr_next
            current._ptr_next = new_node
            new_node._ptr_prev = current
            new_node._ptr_next = next_node
            if next_node:
                next_node._ptr_prev = new_node
            else:
                self._tail_node = new_node

    def delete(self, value):
        current = self._head_node
        while current:
            if current._content == value:
                if current == self._head_node:
                    self._head_node = current._ptr_next
                    if self._head_node:
                        self._head_node._ptr_prev = None
                elif current == self._tail_node:
                    self._tail_node = current._ptr_prev
                    if self._tail_node:
                        self._tail_node._ptr_next = None
                else:
                    current._ptr_prev._ptr_next = current._ptr_next
                    current._ptr_next._ptr_prev = current._ptr_prev
            current = current._ptr_next
