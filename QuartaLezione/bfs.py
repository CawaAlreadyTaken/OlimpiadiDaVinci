def bfs(nodo):
    queue = []
    queue.append(nodo)
    while len(queue) > 0:
        nodo = queue[0]
        if (visited[nodo]):
            queue = queue[1:]
            continue
        for x in graph[nodo]:
            queue.append(x)
        print(nodo, end=' ')
        visited[nodo] = True
        queue = queue[1:]
        

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

#[[2], [0, 3] .....]

visited = [False for _ in range(n)]

bfs(2)
