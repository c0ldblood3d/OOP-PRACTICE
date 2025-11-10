from Stack import Stack

stack = Stack(case_sensitive=False)
stack.push("Hello")
stack.push("WORLD")
stack.push("Python")
print("Размер стека: " , stack.size())
print("Верхний элемент:" , stack.peek()) 
popped = stack.pop()
print("Вытолкнут:", popped) 
print("Размер после pop:" , stack.size())
print("Верхний элемент:" , stack.peek()) 
