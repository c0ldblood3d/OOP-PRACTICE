class NodeItem:
    def __init__(self, item_value):
        self.val = item_value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Обнаружено, возвращен узел {self.val}"

class BinaryTreeSearch:
    def __init__(self):
        self.__start_node = None
    
    def insert_item(self, value):
        if self.__start_node is None:
            self.__start_node = NodeItem(value)
        else:
            self._insert_item_helper(self.__start_node, value)
    
    def _insert_item_helper(self, current_node, value):
        if value <= current_node.val:
            if current_node.left is None:
                current_node.left = NodeItem(value)
            else:
                self._insert_item_helper(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = NodeItem(value)
            else:
                self._insert_item_helper(current_node.right, value)
    
    def find_item(self, value):
        if self.__start_node is None:
            return None
        return self._find_item_helper(self.__start_node, value)
    
    def _find_item_helper(self, current_node, value):
        if current_node is None or current_node.val == value:
            return current_node
        elif value <= current_node.val:
            return self._find_item_helper(current_node.left, value)
        else:
            return self._find_item_helper(current_node.right, value)