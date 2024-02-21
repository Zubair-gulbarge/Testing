# Problem: Reverse a Linked List
# Description: Reverse a singly linked list.
# Code:

# def reverse_linked_list(head):
#     prev = None
#     while head:
#         temp = head.next
#         head.next = prev
#         prev = head
#         head = temp
#     return prev

# Problem: Implement a Stack using Linked List
# Description: Implement a stack data structure using a linked list.
# Code:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
    
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
    
#     def pop(self):
#         if self.is_empty():
#             return None
#         data = self.top.data
#         self.top = self.top.next
#         return data
    
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.top.data
    
#     def is_empty(self):
#         return self.top is None
