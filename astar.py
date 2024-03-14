def astaralgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    
    def heuristic(n):
        H_dist={
            'A':11,
            'B':12,
            'C':20,
            'D':77,
            'E':3,
            'G':0
        }
        return H_dist[n]
    while open_set:
        n=min(open_set,key=lambda x:g[x]+heuristic(x))
        if n==stop_node or Graph_nodes.get(n) is None:
            pass
        else:
            for m,weight in Graph_nodes.get(n,[]):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if not n:
            print("Path doesnot exist")
            return None
        if n==stop_node:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start_node)
            path.reverse()
            return g[stop_node],path
        open_set.remove(n)
        closed_set.add(n)
    print(":Path doesnt exist")
    return None

Graph_nodes={
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    'C':None,
    'D':[('D',6)],
    'E':[('G',1)]
}     
optimal_value_path=astaralgo('A','G')
if optimal_value_path is not None:
    optimal_value, path = optimal_value_path
    print('Optimal value:', optimal_value)
    print('Path:', path)                      