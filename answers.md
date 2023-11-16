# CMPS 2200 Recitation 10## Answers

**Name:** Ella Moses



Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

The work is equal to the number of nodes plus the number of edges. 
W(n) = O(n+m)

- **4)**

Once. If all nodes are reachable by the first node, then the graph is connected and if they are not all reachable by the first node the graph is not connected. So we only need to check the reachable set of one node to determine if the graph is connected. 

- **5)**

The work of connected is equal to the work of reachable since their is one call to reachable.

W(n) = O(n+m)

- **7)**

If we switched to an adjacency matrix, the work is equal to O(n^2). This is because for each node you must check each of the other nodes to see if there is a connection. 