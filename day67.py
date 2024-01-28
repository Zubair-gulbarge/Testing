# Problem: In-order Traversal of a Binary Search Tree (BST)
# Description: Implement the in-order traversal of a binary search tree.
# Code:

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Problem: Finding the Height of a Binary Tree
# Description: Implement a function to find the height of a binary tree.
# Code:
