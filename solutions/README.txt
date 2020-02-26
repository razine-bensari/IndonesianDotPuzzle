Hi TA,

The way our algorithm works is that we generate the whole tree as an adjacency list and then we run the DFS on the tree.

input test #4 and #1 are not being run in enough time because for both case we have to generate 3.8 billion nodes in memory and 6 billions nodes for the other one

its essentially the (size ^ size)^ max_depth.

Because of that solution for input 1 and 4 are too long to compute.

However, we have solutions for the other ones.