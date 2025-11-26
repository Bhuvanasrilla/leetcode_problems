# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        q=head
        while q.next!=None and q.next.next!=None:
            q=q.next.next
            p=p.next
        if q.next!=None:
            return p.next
        else:
            return p
        