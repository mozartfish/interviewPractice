# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current_head = head
        while head.next is not None:
            node = head.next
            head.next = node.next
            node.next = current_head
            current_head = node
    
        return current_head
            
        