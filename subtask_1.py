def check_constraints(graph, source, sink, flow):
    current_vertex = source
    to_visit = [current_vertex]
    source_out = 0
    sink_in = 0

    while to_visit:
        outward = graph.out_edges(current_vertex)
        inward = graph.in_edges(current_vertex)
        total_out_flow = 0
        total_in_flow = 0

        if outward:
            test_out = outward[0]

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

            # Constraint 3: flow splits evenly between edges
            if not is_equal(flow[(current_vertex, out.head)], flow[(current_vertex, test_out.head)]):
                return False

        # Constraint 2: flow in = flow out
        
        # Determine flow going into vertex
        total_in_flow = sum([flow[(inw.tail, current_vertex)] for inw in inward])
        if current_vertex == source:
            source_out = total_out_flow
        elif current_vertex == sink:
            sink_in = total_in_flow
        elif not is_equal(total_in_flow, total_out_flow):
            return False

        if to_visit:
            to_visit.pop(0)
            if to_visit:
                current_vertex = to_visit[0]

    if not is_equal(source_out, sink_in):
        return False
            
    return True