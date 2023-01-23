import java.util.*;
import java.io.*;
class box{
    private box parent;
    private Vector<Integer> position;
    private int g;
    private int h;
    private int f;
    box(box parent = null, Vector<Integer>position = null)
    {
        this.parent = parent;
        this.position = position;
        this.g = 0;
        this.h = 0;
        this.f = 0;
    }

    boolean __eq__(box other)
    {
        return this.position = other.position;
    }
}

public class astar(Vector<Vector<Integer>> maze, Vector<Integer> start,Vector<Integer> end)
{
    // Returns as LinkedList as the result
    box start_node = box(null,start);
    box end_node = box(null,end);

    Vector<box> open_list = new Vector<box>();
    Vector<box> closed_list = new Vector<box>();
    box current_node;
    int current_index;
    open_list.add(start_node);

    while(open_list.size()>0)
    {
        current_node = open_list.get(0);
        current_index = 0;
        Iterator I = open_list.iterator();
        while(I.hasNext())
        {
            if(I.next().f < current_node.f)
            {
                current_node = I.next();
                current_index = I.next
            }
        }
    }
}