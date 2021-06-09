from header_script import *
from main_script import *

graph_b = Graph([1, 2, 4, 3, 6, 5, 7, 8], [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)] + [(2,3), (4,3), (6,5), (6,7)], [5,4,4, 3,7,2, 2,2,1] + [9, 8, 7, 6])

print('In-degrees of vertices in Graph B (Sub-task 0 example)')
for v in graph_b.vertices:
    print(v, in_degree(graph_b, v), sep='\t')
print()