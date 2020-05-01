nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target_value):
    # map that maps value to its index
    value_map = dict()
    for i, value in enumerate(nums):
        # find the difference of the target and its values
        difference = target - value
        if difference in value_map:
            return [value_map[difference], i]
        value_map[value] = i

foo = twoSum(nums, target)
print(foo)
