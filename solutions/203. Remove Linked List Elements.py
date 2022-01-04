# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        c1 = head
        c2 = head.next
        while c2:
            if c2.val == val:
                c1.next = c2.next
                c2 = c2.next
            else:
                c2 = c2.next
                c1 = c1.next
        
        if head.val == val:
            return head.next
        return head
