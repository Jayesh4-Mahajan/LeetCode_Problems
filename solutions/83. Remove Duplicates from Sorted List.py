# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        currNode = head
        nextNode = currNode.next
        while nextNode:
            if currNode.val == nextNode.val:
                currNode.next = nextNode.next
            else:
                currNode = currNode.next
            nextNode = nextNode.next
        return head
