# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        a = ListNode()
        c = a
        while c1 is not None and c2 is not None:
            if c1.val <= c2.val:
                c.next = c1
                c1 = c1.next
            else:
                c.next = c2
                c2 = c2.next
            c = c.next
        if c1 is None: 
            c.next = c2
        else:
            c.next = c1
                
        
        return a.next
