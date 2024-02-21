# Problem: Reverse a Linked List
# Description: Reverse a singly linked list.
# Code:

def reverse_linked_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
