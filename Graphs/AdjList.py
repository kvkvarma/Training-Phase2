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