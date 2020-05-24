# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def NodeIntersection(self, head):
        # define some stuff
        tortoise = hare = head
        
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise
        return None
    
    def detectCycle(self, head: ListNode) -> ListNode:
        # check if the head is null 
        if head is None:
            return None
        
        intersect = self.NodeIntersection(head)
        if intersect is None:
            return None
        
        # use two pointer approach again 
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1
        
        