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

input = [1, 2, 3, 4, 5, 6, 7]
k = 3



def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1
def rotate(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

rotate(input, 3)