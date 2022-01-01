graph = {
    'a':['b'],
    'b':['c'],
    'c':['d'],
    'd':['e'],
    'e':[]
}


def BST(graph,strt_node) -> None:
    queue = [strt_node]
    vals = []

    while queue:
        vertex = queue.pop()
        vals.append(vertex)
        for v in graph[vertex]:
            queue.insert(0,v)
    
    print(vals)


def DFT(graph,strt_node) -> None:
    stack = [strt_node]
    vals = []

    while stack:
        vertex = stack.pop()
        vals.append(vertex)

        for v in graph[vertex]:
            stack.append(v)
    

    print(vals)


def Vertex_reachable(graph,start,end) -> bool:
    queue = [start]

    while queue:
        vertex = queue.pop()

        for v in graph[vertex]:
            if v == end:
                return True
            else:
                queue.insert(0,v)
    
    return False


print(Vertex_reachable(graph,'a','e'))