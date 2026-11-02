# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None :
            return False
        slow_ptr = head
        fast_ptr = head.next

        while slow_ptr!=fast_ptr :
            if fast_ptr.next is None or fast_ptr.next.next is None :
                return False
            slow_ptr=slow_ptr.next
            fast_ptr =fast_ptr.next.next
        
        return True