from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, n, visited, recStack):
        ## mark current node as visited and push it to recstack
        visited[n] = True
        recStack[n] = True

        for neighbor in self.graph[n]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.v
        recStack = [False] * self.v
        for node in range(self.v):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
## get the root as current node
## check if the current node is visited
## if visited check if it in recursion stack
##  if in recursion stack, it means cycle present
##  if not in recursion stack, visit the process and add it to recursion stack
## if not present in recursion stack, visit it and process its neighbor nodes

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
#g.addEdge(1, 2)
#g.addEdge(2, 0)
g.addEdge(2, 3)
#g.addEdge(3, 3)
if g.isCyclic() == 1:
    print "Graph has a cycle"
else:
    print "Graph has no cycle"