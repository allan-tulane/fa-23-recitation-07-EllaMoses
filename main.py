from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node]) #At the start results only has the start node. Once the function ends, this will contain all nodes reachable by the start node
    frontier = set([start_node]) #At the start this constains only the start node, once the funtion ends frontier will be empty
    while len(frontier) != 0: #if frontier is empty no more nodes are reachable so return result
        #update result: add values in frontier to result, use | to avoid having duplicate items
        result_new = result | frontier 
        result = result_new  
        #update frontier
        f = frontier.pop() #remove value from frontier, store this value in f
        frontier_neighbors = graph[f] #find the neighbors of f
        frontier = frontier_neighbors - result #add all of the neighbors to the frontier, subtract the result to make sure there are no duplicates
    return result 


def connected(graph):
    nodes = []
    for key in graph.keys(): #add all keys in the dictionary to the list of nodes
        nodes += key
    connections = reachable(graph, nodes[0]) #find the values reachable by the first node
    #if the first node can reach all values, the graph is connected
    if len(connections) == len(graph):
        return True
    else:
        return False

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if connected(graph) is True:
        return 1
    else:
        keys = list(graph.keys()) #make list of nodes
        start_node = keys[0] #identify start node
        connections = reachable(graph, start_node) #find the connections of the start node, these connection count as 1 component
        for i in connections: #remove all values connected to start node from graph so we can determine if remaining nodes are connected
            graph.pop(i)
        return 1 + n_components(graph) #1 accounts for removed values connected to start_node, then use recursive call on remaining nodes


#graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
print(n_components(graph))