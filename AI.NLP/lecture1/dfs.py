paths = {
    'A' : ['B'], 
    'B' : ['A','C','D','F'], 
    'C' : ['B','E'],
    'D' : ['B'],
    'E' : ['C'],
    'F' : ['B'],
}

def DFS(paths,visited=[],start='A',end = 'C'):
    visited.append(start)
    print(start)
    if start == end: 
        print(' => '.join(visited))
        return visited
    while paths[start]:
        node = paths[start].pop(0)
        if node in visited: continue
        DFS(paths,visited,node)
DFS(paths)
