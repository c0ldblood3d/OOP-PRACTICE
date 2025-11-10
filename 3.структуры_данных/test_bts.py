from BinaryTreeSearch import NodeItem, BinaryTreeSearch
import random

bts = BinaryTreeSearch()
for i in range(21):
    num = random.randint(1, 38)
    bts.insert_item(num)
    print(f"Вставлено число: {num}")

print("\nПоиск элементов:")
print("11 ->", bts.find_item(11))
print("50 ->", bts.find_item(50))
print("29 ->", bts.find_item(29))