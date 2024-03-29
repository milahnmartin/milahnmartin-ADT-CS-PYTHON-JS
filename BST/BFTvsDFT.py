class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.right = None
        self.left = None


def insert(root,val) -> Node:
    if root is None:
        return Node(val)
    else:
        if root.val == val:
            return root
        elif val > root.val:
            root.right = insert(root.right,val)
        else:
            root.left = insert(root.left,val)
    
    return root


def DFT(start_node) -> list:
    stack = [start_node]
    vals_order = []

    while stack:
        curr_node = start_node.pop()
        vals_order.append(curr_node.val)

        if curr_node.right:
            stack.append(curr_node.right)
        
        if curr_node.left:
            stack.append(curr_node.left)

    
    return vals_order

def BST(start_node) -> list:
    vals_order = []
    queue = [start_node]

    while queue:
        curr_node = queue.pop()
        vals_order.append(curr_node.val)


        if curr_node.right:
            queue.insert(0,curr_node.right)
        

        if curr_node.left:
            queue.insert(0,curr_node.left)
    
    return vals_order
    
        

def Smallest(root):
    if root.left is None:
        return root.val
    else:
        return Smallest(root.left)
    

def Biggest(root):
    if root.right is None:
        return root.val
    else:
        return Biggest(root.right)

r = Node(50)
r = insert(r,90)
r = insert(r,10)
r = insert(r,50)
r = insert(r,100)
r = insert(r,2)



print(Smallest(r))
