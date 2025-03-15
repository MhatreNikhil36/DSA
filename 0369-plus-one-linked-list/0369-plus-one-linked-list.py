# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        s=head
        stack=[]
        while s:
            stack.append(s)
            s=s.next
        c=0
        x=stack.pop()
        if x.val>=9:
            x.val=0
            c=1
        else:
            x.val+=1
        while stack and c==1:
            x=stack.pop()
            if x.val>=9:
                x.val=0
                c=1
            else:
                x.val+=1
                c=0
        if c==1:
            nh=ListNode(1,head)
            head=nh
        return head 

