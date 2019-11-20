# mst-solver
Minimum Spanning tree solver. Implemented based Kruskal's algorithm using a d-heap as
a priority queue of edges and rooted trees for disjoint sets.

Input graph has to be in DIMACS graph format

Example input can be found in sample_input.txt


example run:

./mstsolve -d 2 -i input_graph.txt -o output_file

where
 d = depth of d-heap (edge priority queue)
 i = input file
 o = output file
