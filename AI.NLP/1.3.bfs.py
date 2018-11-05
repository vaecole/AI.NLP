paths = {
    'A' : ['B'], 
    'B' : ['A','C','D','F'], 
    'C' : ['B','E'],
    'D' : ['B'],
    'E' : ['C'],
    'F' : ['B'],
}

def BFS(paths,start='D',end = 'A'):
    queue = []
    visited = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node)
        visited.append(node)
        if node == end:
            return visited
        while paths[node]:
            next_node = paths[node].pop(0)
            if next_node in visited: continue
            queue.append(next_node)        
print(' => '.join(BFS(paths)))