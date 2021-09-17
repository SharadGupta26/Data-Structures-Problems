class Node :
    def __init__(self, data) -> None:
        self.val = data
        self.next = None

class LinkedList :
    def __init__(self) -> None:
        self.head = None