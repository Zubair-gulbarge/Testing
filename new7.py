def sum_of_list_elements(input_list):
    total = 0
    for element in input_list:
        total += element
    return total

# Example usage:
input_list = [1, 2, -8]
result = sum_of_list_elements(input_list)
print("Sum of elements:", result)
