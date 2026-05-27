class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
a = Node(5)
b = Node(6)
c = Node(7)

a.next=b
b.next=c

head = a
# print(head.value)
# print(head.next.value)
# print(head.next.next.value)

# Traversal
curr = head
while curr is not None:
    print(curr.value)
    curr = curr.next