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
            current_pointer = next_pointer
        
        self.head = prev_pointer

    
    def middle_point(self) -> Node:
        if self.head is None:
            return None

        fast_pointer = self.head
        slow_pointer = self.head
        

        while slow_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        

        return slow_pointer
    
    def perfect_print(self) -> None:
        if self.head is None:
            return
        
        curr_vals = []
        next_vals = []

        curr_node = self.head
        while curr_node:
            if curr_node.next is None:
                curr_vals.append(curr_node.val)
                next_vals.append(None)
            else:
                curr_vals.append(curr_node.val)
                next_vals.append(curr_node.next.val)
            
            curr_node = curr_node.next


        for c,n in zip(curr_vals,next_vals):
            print(f'Curr-Node:{c}, Next-Node:{n}')



l = sllist()


for i in range(501):
    l.add_tail(i)


l.perfect_print()
print(l.middle_point().val)