# practice
# # singly linked list

# # how to create a linked list
# class Node:
#     def __init__(self,data):
#         self.data= data 
#         self.next= None 


# node_a = Node(5)
# node_b= Node(3)
# node_c= Node(7)

# node_a.next= node_b
# node_b.next= node_c
# node_c.next= None

# head = node_a

# # traverse linked list
# def printLinkedList(head):

#     current = head

#     while current:
#         print(current.data, end= " -> ")
#         current = current.next
#     print("None")

# printLinkedList(head) 


# # insertion at the beginning
# NewNode= Node(4)
# NewNode.next= head
# head = NewNode
# printLinkedList(head) 

# # insertion at the end
# # def addatend(head):
# NewNode = Node(1)
# current = head 
# while current.next != None:
#     current = current.next 
# current.next= NewNode
# printLinkedList(head) 

# # insertion in kth index
# k = 2
# newNode= Node(6)
# current= head
# for i in range(k-1):
#     current = current.next
# newNode.next = current.next
# current.next = newNode
# printLinkedList(head) 

# # delete the first node
# head = head.next
# printLinkedList(head)

# # delete the last node
# current = head 
# while current.next.next != None:
#     current= current.next 
# current.next= None 
# printLinkedList(head)

# # 5 -> 6 -> 3 -> 7 -> 1 -> None
# # h 
# #                 c
 
# #delete the kth index node
# k =2 
# current = head
# for i in range(k-1):
#     current= current.next
# current.next= current.next.next
# printLinkedList(head)

# doubly linked list
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next= None 
        self.prev = None 
    
a= DoublyNode(5)
b= DoublyNode(3)
c= DoublyNode(7)

a.next= b 

b.next= c 
b.prev= a 

c.prev= b

curr = a
while curr:
    print(curr.data, end=" <-> ")
    curr = curr.next


