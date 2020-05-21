# input = [7, 1, 5, 3, 6, 4]
#
# def buySellStock(input):
#     # variable for keeping track of the maximum profit
#     max_profit = 0
#     for j in range(1, len(input)):
#         if input[j] > input[j - 1]:
#             max_profit += input[j] - input[j - 1]
#     return max_profit
#
#
# print(buySellStock(input))

# input = [1, 2, 3, 4, 5, 6, 7]
# k = 3
#
#
#
# def reverse(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start, end = start + 1, end - 1
# def rotate(arr, k):
#     n = len(arr)
#     k %= n
#     reverse(arr, 0, n - 1)
#     reverse(arr, 0, k - 1)
#     reverse(arr, k, n - 1)
#
# rotate(input, 3)

input = [4, 1, 2, 1, 2]
def singleNumber(arr):
    arr.sort()
    i = 0
    while i in range(len(arr)):
        value = arr[i]
        sub_arr = arr[i + 1:]
        if value in sub_arr:
            i = sub_arr.index(value)
            arr = sub_arr[i + 1:]
            print(i)
        else:
            return arr[i]
    # for i in range(len(arr)):
    #     value = arr[i]
    #     sub_arr = arr[i + 1:]
    #     if value in sub_arr:
    #         i = sub_arr.index(value) + 1
    #         continue
    #     else:
    #         return arr[i]


# singleNumber(input)

input1 = [1, 2, 2, 1]
input2 = [2, 2]

thing = set(input1)
print(thing)

def twoArray(nums1, nums2):
    result = dict()
    for num in nums1:
        if num not in result:
            result[num] = 0
        result[num] += 1

    final_result = []
    for num in nums2:
        if num in result and result[num] > 0:
            result[num] -=1
            final_result.append(num)
    return final_result

twoArray(input1, input2)