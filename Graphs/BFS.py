def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True
    while Q:
        currNode = Q.pop(0)
        result.append(currNode)
 
        for neighbour in adj[currNode]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
def printBFSTraversal(adj, n):
    visited = [False] * (n+1)
    result = []
    for node in range(1,n+1):
        if visited[node] == False:
            initiateBFSTraversal(node,visited, adj, result)
    print("BFS Traversal is: ", result)
 
 
 
n,m=map(int,input().split())
#n is no of nodes
#m is no of edges
adj=[]
for i in range(n+1):
    adj.append([])
    
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
    
print(adj)

#print(adj)
printBFSTraversal(adj, n)