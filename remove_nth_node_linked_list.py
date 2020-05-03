# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0)
        
        dummy_node.next = head
        
        first_node = dummy_node
        second_node = dummy_node
        
        # got the index we want
        for j in range(n + 1):
            first_node = first_node.next
        
        while first_node is not None:
            first_node = first_node.next
            second_node = second_node.next
        
        second_node.next = second_node.next.next 
        
        return dummy_node.next