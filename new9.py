def two_sum(nums, target):
    complement_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_dict:
            return [complement_dict[complement], i]
        complement_dict[num] = i
    return None
