
from collections import defaultdict

class Graph:
     
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        print(self.graph)

    def BFS(self, s):
        mini=s
        count=-1
        cost=[0,0,0,0,0] 
        depth=[-1,-1,-1,-1,-1]
        cost[s] = count
        depth[s]=0
        
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            r=s
            s = queue.pop(0)
            count+=1
            print (s, end = " ")
            if (mini>s):
                mini=s
                cost[s] = count
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                depth[s]=depth[r]+1
            print("{",f"{s}, {r}, Move, 1, ", depth[s]-1,"}")
        print('\nminimum number in node : ',mini,"\ncost is :",cost[mini])
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
start=int(input("enter the starting vertex : "))
g.BFS(start)
