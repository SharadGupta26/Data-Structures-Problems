class Node :
    def __init__(self, data) -> None:
        self.val = data
        self.next = None
    def __str__(self) -> str:
        res = [self.val]
        tmp = self.next
        while tmp :
            res.append(tmp.val)
            tmp = tmp.next
        return str(res)

class LinkedList :
    def __init__(self) -> None:
        self.head = None
    def __str__(self) -> str:
        return str(self.head)

