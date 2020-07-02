# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        if head is None:
            return True
        curr = head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
            
        return values == values[::-1]