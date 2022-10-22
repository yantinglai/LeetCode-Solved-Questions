# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # dummy - 1 - 2 
           # s          f  
        if not head or not head.next: return 
        
        dummy = ListNode(0)
        dummy.next = head 
        
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next 
            
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next 
        
        slow.next = slow.next.next 
        
        
        return dummy.next 
    
    # slow.next is already a none, 
        
        
        