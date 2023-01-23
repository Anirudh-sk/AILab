import java.io.*;
import java.util.*;
public class Graph{
    private int V;
    private LinkedList<Integer> adj[];
    public boolean found;
    @SuppressWarnings("unchecked") Graph(int v)
    {
        V = v;
        adj = new LinkedList[v];
        found = false;
        for(int i =0; i<v; ++i)
        {
            adj[i] = new LinkedList();
        }
    }

    void addEdge(int v, int w)
    {
        adj[v].add(w);
    }

    void DfsUtil(int v, boolean visited[], int key){
        visited[v] = true;
        // System.out.println(v + " ");
        if(v == key){
            System.out.println("The key: "+key+" is connected to root");
            this.found = true;
            return;
        }
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext())
        {
            int n = i.next();
            if(!visited[n])
                DfsUtil(n, visited, key);
        }
    }

    void Dfs(int key)
    {
        boolean visited[] = new boolean[V];
        DfsUtil(0, visited, key);
    }

    public static void main(String[] args)
    {
        Graph g = new Graph(5);
        g.addEdge(0,1);
        g.addEdge(2,0);
        g.addEdge(4,3);
        g.addEdge(0,4);
        g.addEdge(3,1);
        g.Dfs(1);
        if(!g.found)
        {
            System.out.println("The Key is not found");
        }
    }
}