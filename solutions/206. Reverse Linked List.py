# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        currNode = head
        prevNode = None
        nextNode = head.next
        while nextNode:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
        currNode.next =prevNode
        return currNode
