from node import Node
from singleLinkedList import Linkedlist

nums = Linkedlist()
nums.insertion(1)
print("List Length: %d"%nums.length)
nums.insertion(2)
print("List Length: %d"%nums.length)
nums.insertion(4)
print("List Length: %d"%nums.length)
nums.insertion(7)
print("List Length: %d"%nums.length)
nums.insertion(5, 3.5)
print("List Length: %d"%nums.list_length())
nums.insertion(6, 4.5)
print("List Length: %d"%nums.list_length())
nums.insertion(3, 3)
print("List Length: %d"%nums.list_length())

while nums.head != None:
    print(nums.head.data)
    nums.head = nums.head.get_next()