import re
from typing import ChainMap
from header_script import *

def in_degree(graph, vertex):
    return len(graph.in_edges(vertex))

def check_constraints(graph, source, sink, flow):
    current_vertex = source
    to_visit = [current_vertex]

    while to_visit:
        outward = graph.out_edges(current_vertex)
        inward = graph.in_edges(current_vertex)
        total_out_flow = 0
        total_in_flow = 0
        
        for out in outward:
            flow_cost = flow[(current_vertex, out.head)]
            capacity = out.capacity

            # Constraint 1: flow <= capacity
            if flow_cost > capacity:
                return False
            total_out_flow += flow_cost

            # Remove redundant visit
            if out.head not in to_visit:
                to_visit.append(out.head)

        # Constraint 2: flow in = flow out
        total_in_flow = 0
        if current_vertex != source and current_vertex != sink:
            # Determine flow going into vertex
            total_in_flow = sum([flow[(inw.tail, current_vertex)] for inw in inward])

            if total_in_flow != total_out_flow:
                return False

            # Constraint 3: flow splits evenly between edges
            expected_flow_split_cost = total_in_flow/len(outward)
            for out in outward:
                flow_cost = flow[(current_vertex, out.head)]
                if not is_equal(flow_cost, expected_flow_split_cost):
                    return False

        if to_visit:
            to_visit.pop(0)
            if to_visit:
                current_vertex = to_visit[0]

    return True

    

def is_feasible(graph, source, sink, flow_value):
    pass

def max_equal_split_flow(graph, source, sink):
    pass

def max_equal_split_flow_upgrade(graph, source, sink):
    pass

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