from header_script import *

def in_degree(graph, vertex):
    return len(graph.in_edges(vertex))

def check_constraints(graph, source, sink, flow):
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')

def is_feasible(graph, source, sink, flow_value):
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')
        
def max_equal_split_flow(graph, source, sink):
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')

def max_equal_split_flow_upgrade(graph, source, sink):
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')

def grid_graph(width, height, common_capacity):
    vertices = [(x,y) for x in range(width + 1) for y in range(height + 1)]
    capacities = [common_capacity for _ in range(width*(height + 1) + height*(width + 1))]
    edges = [((x,y),(x + 1, y)) for x in range(width) for y in range(height + 1)] + [((x,y),(x, y + 1)) for x in range(width + 1) for y in range(height)]

    return Graph(vertices, edges, capacities)

def grid_graph_pseudorandom(width, height, seed):
    vertices = [(x,y) for x in range(width + 1) for y in range(height + 1)]
    edges = [((x,y),(x + 1, y)) for x in range(width) for y in range(height + 1)] + [((x,y),(x, y + 1)) for x in range(width + 1) for y in range(height)]

    capacities = [0 for _ in range(width*(height + 1) + height*(width + 1))]
    capacities[0] = seed
    for i in range(1, len(edges)):
        capacities[i] = (8121*capacities[i - 1] + 28411) % 134456
    
    for i in range(len(capacities)):
        capacities[i] = 1 + (capacities[i] % 100)
    
    return Graph(vertices, edges, capacities)