# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=None
        fast=head
        if not fast.next:
            return None
        while fast and fast.next:
            fast=fast.next.next
            if not slow:
                slow=head
            else:
                slow=slow.next
        slow.next=slow.next.next
        return head
