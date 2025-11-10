from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
print("Initial Doubly Linked List:")
dll.display()   

dll.insert(25)
print("After inserting 25 in middle:")
dll.display()  

dll.delete(25)
print("After deleting 25:")
dll.display()  
