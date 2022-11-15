def dfs(nodo):
    if (visited[nodo]):
        return
    visited[nodo] = True
    print(nodo)
    for x in graph[nodo]:
        dfs(x)

with open("input.txt", 'r') as f:
    lines = f.readlines()

n = int(lines[0].split(' ')[0])
m = int(lines[0].replace("\n", "").split(' ')[1])

graph = [[] for _ in range(n)]
for i in range(m):
    a = int(lines[1+i].split(' ')[0])
    b = int(lines[1+i].replace("\n", "").split(' ')[1])
    graph[a].append(b)
print(graph)

visited = []
for i in range(n):
    visited.append(False)

dfs(0)

