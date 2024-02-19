# Problem: Find the Maximum Subarray Sum
# Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Code:

# def max_subarray(nums):
#     max_sum = float('-inf')
#     current_sum = 0
#     for num in nums:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# Problem: Implement Depth First Search (DFS)
# Description: Implement the depth first search algorithm to traverse a graph.
# Code:

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)

# Problem: Find the Longest Palindromic Substring
# Description: Given a string s, find the longest palindromic substring in s.
# Code:

# def longest_palindrome(s):
#     longest = ''
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             substring = s[i:j+1]
#             if substring == substring[::-1] and len(substring) > len(longest):
#                 longest = substring
#     return longest

# Problem: Merge Two Sorted Lists
# Description: Merge two sorted linked lists and return it as a new sorted list.
# Code:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
