from header_script import *
from main_script import *

import itertools

if __name__ == '__main__':
    graph_a = Graph(list(range(1,9)), [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)], [5,4,4, 3,7,2, 2,2,1])
    graph_b = Graph([1, 2, 4, 3, 6, 5, 7, 8], [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)] + [(2,3), (4,3), (6,5), (6,7)], [5,4,4, 3,7,2, 2,2,1] + [9, 8, 7, 6])
    graph_c = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2])
    graph_d = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)] + [(2,6), (4,8)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2] + [6, 3])
    
    print('Brute-force enumeration of integer-valued feasible flows on a 2x1 grid using check_constraints:')
    
    tiny_grid = grid_graph(2, 1, 6)
    E = tiny_grid.edges
    a = 0
    b = 0
    for flow_values in itertools.product(range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7)):
        a += 1
        flow = dict()
        for i in range(len(E)):
            flow[(E[i].tail, E[i].head)] = flow_values[i]

        if check_constraints(tiny_grid, (0,0), (2,1), flow):
            b += 1
            # print(flow)
    print(a, b)