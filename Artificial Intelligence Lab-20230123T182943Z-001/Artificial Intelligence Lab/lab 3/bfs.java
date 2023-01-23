import java.util.*;
import java.io.*;
public class bfs
{
    private int V;
    private LinkedList<Integer> adj[]; 
    private boolean found;
    bfs(int v)
    {
        V = v;
        found = false;
        adj = new LinkedList[v];
        for(int i=0; i<v; ++i)
        {
            adj[i] = new LinkedList(); 
            }
        }
    void addEdge(int v, int w)
    {
        adj[v].add(w);
 
    }
    void bfs(int s, int key)
    {
        boolean visited[] = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<Integer>();
        visited[s] = true;
        queue.add(s);
        while(queue.size() != 0)
        {
            s = queue.poll();
            if(s == key){
                System.out.println("The Key "+s+" was found");
                found = true;
                break;
            }
            System.out.println();
            System.out.println(s);
            Iterator<Integer> i = adj[s].listIterator();
            while(i.hasNext())
            {
                int n = i.next();
                if (!visited[n]){
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
    public static void main(String[] args)
    {
        Scanner in1 = new Scanner(System.in);
        int size = in1.nextInt();
        bfs g = new bfs(size);
        int a, b, c;
        c = in1.nextInt();
        for(int j =0; j<c; j++)
        {
            System.out.println("Enter parent");
            a = in1.nextInt();
            System.out.println("Enter child");
            b = in1.nextInt();
            g.addEdge(a,b);
        }
        // g.addEdge(0,4);
        // g.addEdge(0,2);
        // g.addEdge(1,4);
        // g.addEdge(4,1);
        // g.addEdge(0,3);
        // g.addEdge(1,2);
        // g.addEdge(2,4);
        System.out.println("Enter the key you want to find");
        Scanner in = new Scanner(System.in);
        int key = in.nextInt();
        g.bfs(0, key);
        if(!g.found)
        {
            System.out.println("The Key "+key+" was not found");
    }

}
}