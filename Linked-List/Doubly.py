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
    
    def iterate(self):
        if self.head is None:
            return None
        
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
    
    def reverse_list(self) -> None:
        if self.head is None:
            return
        
        prev_pointer = None
        next_pointer = None
        current_pointer = self.head

        while current_pointer:
            next_pointer = current_pointer.next
            current_pointer.next = prev_pointer
            prev_pointer = current_pointer
            current_pointer.prev = next_pointer
            current_pointer = next_pointer
        
        self.head = prev_pointer
    

    def perfect_print(self) -> None:
        if self.head is None:
            return
        
        curr_node = []
        prev_node = []
        next_node = []

        curr = self.head

        while curr:
            if curr.prev is None:
                prev_node.append(None)
                curr_node.append(curr.val)
                next_node.append(curr.next.val)
            elif curr.next is None:
                prev_node.append(curr.prev.val)
                curr_node.append(curr.val)
                next_node.append(None)
            else:
                prev_node.append(curr.prev.val)
                curr_node.append(curr.val)
                next_node.append(curr.next.val)
            
            curr = curr.next

        

        for p,c,n in zip(prev_node,curr_node,next_node):
            print(f'Prev-Node:{p}, Curr-Node:{c}, Next-Node:{n}')




p = dllist()


for i in range(5,500,3):
    p.add_tail(i)

p.perfect_print()
print(f'[REVERSED DOUBLY LINKED LIST]')
p.reverse_list()
p.perfect_print()
