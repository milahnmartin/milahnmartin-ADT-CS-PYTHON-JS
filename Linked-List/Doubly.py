class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class dllist:
    def __init__(self) -> None:
        self.head = None
    
    def add_head(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        
        new_node = Node(val)

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def add_tail(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        
        curr_node = self.head
        new_node = Node(val)

        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = new_node
        new_node.prev = curr_node
        
