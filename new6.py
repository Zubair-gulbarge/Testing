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

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

# Example usage:
my_todo_list = ToDoList()
my_todo_list.add_task("Buy groceries")
my_todo_list.add_task("Finish work project")
my_todo_list.list_tasks()
my_todo_list.remove_task("Buy groceries")
my_todo_list.list_tasks()
