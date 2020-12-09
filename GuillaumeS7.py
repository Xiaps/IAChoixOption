from pycsp3 import *

nNodes, edges = data
nColors = 4
# x[i] is the color assigned to the ith node of the graph
x = VarArray(size=nNodes, dom=range(0,nColors))

satisfy(
    # two adjacent nodes must be colored differently
    x[i] != x[j] for (i, j) in edges
)

