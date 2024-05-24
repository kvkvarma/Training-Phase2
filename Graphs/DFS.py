def initiateDFSTraversal(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * (n+1)
    for node in range(1,n+1):
        if visited[node] == False:
            initiateDFSTraversal(node, visited, adj, result)
 
    print("DFS Traversal is: ", result)
 
 
 
n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n+1):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
#printBFSTraversal(adj, n)
printDFSTraversal(adj, n)