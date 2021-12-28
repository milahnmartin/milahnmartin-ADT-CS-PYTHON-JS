class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None


class sllist:
    def __init__(self) -> None:
        self.head = None
    
    def add_head(self,val) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node
    
    def add_tail(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        
        new_node = Node(val)
        current_node = self.head

        while current_node.next:
            current_node = current_node.next


        current_node.next = new_node
    

    def list_size(self) -> int:
        list_counter = 0
        current_node = self.head

        if self.head is None:
            return 0
        elif self.head.next is None:
            return 1

        
        while current_node:
            list_counter +=1
        
        return list_counter
    

    def iterate_list(self) -> list:
        vals = []

        if self.head is None:
            return []
        else:
            current_node = self.head
            while current_node:
                vals.append(current_node.val)
                current_node = current_node.next
            
            return vals
    
    def middle_point(self) -> Node:
        if self.head is None:
            return None

        fast_pointer = self.head
        slow_pointer = self.head
        

        while slow_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        

        return slow_pointer
