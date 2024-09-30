# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.val
            if temp == 0 and not curr.next:
                prev.next = None
            elif temp == 0:
                if prev: prev.next = curr
                prev = curr
            else:
                prev.val += temp
            curr = curr.next
        return head
        