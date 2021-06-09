from header_script import *
from main_script import *

import itertools

if __name__ == '__main__':
    graph_a = Graph(list(range(1,9)), [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)], [5,4,4, 3,7,2, 2,2,1])
    graph_b = Graph([1, 2, 4, 3, 6, 5, 7, 8], [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)] + [(2,3), (4,3), (6,5), (6,7)], [5,4,4, 3,7,2, 2,2,1] + [9, 8, 7, 6])
    graph_c = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2])
    graph_d = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)] + [(2,6), (4,8)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2] + [6, 3])

    print()
    print('Expected output for sample graphs given in MP specifications PDF')
    print('ID', 'no upgrade', 'with upgrade', sep='\t')
    sample_graph = {'A': graph_a, 'B': graph_b, 'C': graph_c, 'D': graph_d}
    source_vertex = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    sink_vertex = {'A': 8, 'B': 8, 'C': 9, 'D': 9}

    for graph_id in sample_graph:
        ans_no_upgrade = max_equal_split_flow(sample_graph[graph_id], source_vertex[graph_id], sink_vertex[graph_id])
        ans_with_upgrade = max_equal_split_flow_upgrade(sample_graph[graph_id], source_vertex[graph_id], sink_vertex[graph_id])

        print(graph_id, "{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')

    print()
    print('Expected output for a pseudorandom 20x20 square grid')
    print('no upgrade', 'with upgrade', sep='\t')
    for seed in range(10):
        medium_grid = grid_graph_pseudorandom(20, 20, seed)

        ans_no_upgrade = max_equal_split_flow(medium_grid, (0,0), (20,20))
        ans_with_upgrade = max_equal_split_flow_upgrade(medium_grid, (0,0), (20,20))

        print("{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')

    print()
    print('Expected output for a pseudorandom 100x100 square grid')
    print('no upgrade', 'with upgrade', sep='\t')
    for seed in range(10):
        large_grid = grid_graph_pseudorandom(100, 100, seed)

        ans_no_upgrade = max_equal_split_flow(large_grid, (0,0), (100,100))
        ans_with_upgrade = max_equal_split_flow_upgrade(large_grid, (0,0), (100,100))

        print("{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')