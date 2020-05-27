# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime complexity: O(n) since we iterate through all the nodes in the list
# Space complexity: O(1) additional space since we don't use any other data structures
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        curr = head
        
        while head.next:
            node = head.next
            head.next = node.next
            node.next = curr
            curr = node
        
        return curr