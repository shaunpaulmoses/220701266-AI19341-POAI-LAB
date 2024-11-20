def get_neighbors(v, adjac_lis):
    return adjac_lis[v]

def h(n):
    # Heuristic function (estimate of cost from n to goal)
    H = {
        'A': 4,  # Assuming heuristic values based on distance to 'D'
        'B': 3,
        'C': 2,
        'D': 0  # Goal node heuristic is 0
    }
    return H[n]

def a_star_algorithm(start, stop, adjac_lis):
    open_lst = set([start])  # Nodes to be evaluated
    closed_lst = set([])     # Nodes already evaluated
    poo = {}                 # g(n): cost from start to node
    poo[start] = 0
    par = {}                 # Parent of each node for path reconstruction
    par[start] = start

    while len(open_lst) > 0:
        n = None
        # Select the node with the lowest f = g + h
        for v in open_lst:
            if n is None or poo[v] + h(v) < poo[n] + h(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == stop:
            reconst_path = []
            while par[n] != n:
                reconst_path.append(n)
                n = par[n]
            reconst_path.append(start)  # Add start node
            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # Update costs and parents for neighbors
        for (m, weight) in get_neighbors(n, adjac_lis):
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                par[m] = n
                poo[m] = poo[n] + weight
            else:
                if poo[m] > poo[n] + weight:
                    poo[m] = poo[n] + weight
                    par[m] = n
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        open_lst.remove(n)
        closed_lst.add(n)

    print('Path does not exist!')
    return None


# Example Graph with adjacency list format
adjac_lis = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []  # Goal node has no outgoing edges
}

# Run A* algorithm
a_star_algorithm('A', 'D', adjac_lis)
