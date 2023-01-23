graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[],
}

visited = set()

def dfs(graph,node):
    global visited
    if node not in visited:
        visited.add(node)
        for n in graph[node]:
            dfs(graph,n)

search=input("Enter the element you want to search : ")
dfs(graph,'A')
print(visited)
if search.upper() in visited:
    print("Element Found")
else:
    print("Element NOT Found")