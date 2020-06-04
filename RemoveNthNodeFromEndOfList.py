# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# runtime complexity: O(n) because of the for and while loop
# space time complexity: O(1) additional space since we do not use another data structure
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        fast = head
        slow = head
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if not prev:
            head = head.next
        else:
            prev.next = slow.next
        
        return head
            
        