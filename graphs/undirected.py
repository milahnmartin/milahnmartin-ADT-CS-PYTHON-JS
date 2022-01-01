graph = {
    'a':['b'],
    'b':['c'],
    'c':['d'],
    'd':['e'],
    'e':[]
}


def bft(graph,start)-> None:
    queue = [start]
    vals = []
    while queue:
        vertex = queue.pop()
        vals.append(vertex)
        for v in graph[vertex]:
            queue.insert(0,v)
    

    print(vals)

def dft(graph,start) -> None:
    stack = [start]
    vals = []
    while stack:
        vertex = stack.pop()
        vals.append(vertex)
        for v in graph[vertex]:
            stack.append(v)


    print(vals)

dft(graph,'a')
print(f'BST NOW \n')
bft(graph,'a')