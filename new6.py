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
