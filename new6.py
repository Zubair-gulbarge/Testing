# def transpose_matrix(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     transposed = [[0] * rows for _ in range(cols)]
#     for i in range(rows):
#         for j in range(cols):
#             transposed[j][i] = matrix[i][j]
#     return transposed

# # Example usage:
# original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_matrix = transpose_matrix(original_matrix)
# for row in transposed_matrix:
#     print(row)

# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)

#     def list_tasks(self):
#         for i, task in enumerate(self.tasks, start=1):
#             print(f"{i}. {task}")

# # Example usage:
# my_todo_list = ToDoList()
# my_todo_list.add_task("Buy groceries")
# my_todo_list.add_task("Finish work project")
# my_todo_list.list_tasks()
# my_todo_list.remove_task("Buy groceries")
# my_todo_list.list_tasks()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self, root):
#         self.root = Node(root)

#     def print_tree(self, traversal_type):
#         if traversal_type == "preorder":
#             return self.preorder_print(tree.root, "")
#         else:
#             return "Invalid traversal type"

#     def preorder_print(self, start, traversal):
#         if start:
#             traversal += (str(start.data) + " ")
#             traversal = self.preorder_print(start.left, traversal)
#             traversal = self.preorder_print(start.right, traversal)
#         return traversal

# # Example usage:
# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# print("Preorder traversal:", tree.print_tree("preorder"))
