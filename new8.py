# # Take the input string from the user
# s = input("Enter a string: ")

# # Take the number of characters to display from the user
# n = int(input("Enter the number of characters from the right: "))

# # Display the last n characters from the right of the string
# if n >= 0:
#     result = s[-n:]
#     print(f"The last {n} characters from the right: {result}")
# else:
#     print("Invalid input for the number of characters.")

# Enter a string: String Slicing in Python
# Enter the number of characters from the right: 5
# The last 5 characters from the right: ython

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] == 9, so the output is [0, 1].

def two_sum(nums, target):
    # Create a dictionary to store the complement of each number along with its index
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in complement_dict:
            # If found, return the indices of the two numbers
            return [complement_dict[complement], i]

        # If not found, add the current number and its index to the dictionary
        complement_dict[num] = i

    # If no solution is found
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
