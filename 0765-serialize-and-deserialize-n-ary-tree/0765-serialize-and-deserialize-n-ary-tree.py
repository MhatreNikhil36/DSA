"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root==None:
            return ''
        q=[str(root.val),'n']
        tq=deque([root])
        while tq:
            curr=tq.popleft()
            if curr.children:
                for  x in curr.children:
                    tq.append(x)
                    q.append(str(x.val))
            else:
                q.append('NULL')
            q.append('n')
        # print(q)
       
        return '|'.join(q)
            

        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data=='':
            return None
        data=deque(data.split('|'))
        start= Node(data.popleft())
        q=deque([start])
        data.popleft()
        # print(data)
        while q:
            c=q.popleft()
            
            while data[0]!='n':
                val=data.popleft()
                if val=='NULL':
                    break
                n=Node(val)
                q.append(n)
                c.children.append(n)
            # print('node',c.val)
            # print('\n children',c.children)
            data.popleft()
        return start

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))