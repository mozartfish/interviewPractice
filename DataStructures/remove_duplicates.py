nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]

def remove(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


print(remove(nums))