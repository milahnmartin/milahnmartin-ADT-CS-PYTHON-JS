graph = {
    'a':['b'],
    'b':['a','c'],
    'c':['b','d'],
    'd':['e'],
    'e':['d']
}


def bft(graph,start)-> None:
    queue = [start]
    vals = []
    while queue:
        vertex = queue.pop()
        vals.append(vertex)
        for v in graph[vertex]:
            if v in vals:
                continue
            else:
                queue.insert(0,v)
    

    print(vals)

def dft(graph,start) -> None:
    stack = [start]
    vals = []
    while stack:
        vertex = stack.pop()
        vals.append(vertex)
        for v in graph[vertex]:
            if v in vals:
                continue
            else:
                stack.append(v)


    print(vals)

dft(graph,'a')
print(f'BST NOW \n')
bft(graph,'a')