# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        l[k-1], l[-k] = l[-k], l[k-1]
        curr = head
        for v in l:
            curr.val = v
            curr = curr.next
​
        return head
