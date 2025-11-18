def two_sum(nums, target):
    list = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in list:
            return [list[diff], i]
        list[num] = i

    return None
nums = [1,2,3,6,7,5]
target = 12
print(two_sum(nums, target))
