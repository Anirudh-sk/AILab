graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[],
}

path = set()

def bfs(graph, start):
    global path
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.add(vertex)
            queue.extend(set(graph[vertex]) - set(path))
    


search=input("Enter the element you want to search : ")
bfs(graph,'A')
print (path)
if search.upper() in path:
    print("Element Found")
else:
    print("Element NOT Found")