class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        mp = head
        while mp:
            mc = m
            nc = n
            
            # Move mc steps forward to find the end of the segment to keep
            while mc > 1 and mp:
                mp = mp.next
                mc -= 1
            
            if not mp:
                break
            
            # Move n steps forward to skip the segment to delete
            nNode = mp.next
            while nc > 0 and nNode:
                nNode = nNode.next
                nc -= 1
            
            # Link the current segment to the next valid segment
            mp.next = nNode
            mp = nNode
        
        return head
