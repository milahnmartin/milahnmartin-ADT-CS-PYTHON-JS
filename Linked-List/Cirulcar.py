class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class cllist:
    def __init__(self) -> None:
        self.head = None
    

    def add(self,new_val) -> None:
        if self.head is None:
            self.head = Node(new_val)
            return
        
        curr_head = self.head

        while curr_head.next != self.head:
            curr_head = curr_head.next
        
        curr_head.next = new_val
        self.head = new_val