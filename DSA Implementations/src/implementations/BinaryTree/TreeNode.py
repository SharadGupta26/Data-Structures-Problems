from collections import deque
class TreeNode :
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.val)

class Tree:
    def __init__(self) -> None:
        self.root = None
        
    def __str__(self) -> str:
        data = []
        if(self.root) :
            elem = deque([self.root])
            while elem :
                size = len(elem)
                while size :
                    size -= 1
                    i = elem.popleft()
                    data.append(i.val)
                    if i.left :
                        elem.append(i.left)
                    if i.right : 
                        elem.append(i.right)
        return str(data)