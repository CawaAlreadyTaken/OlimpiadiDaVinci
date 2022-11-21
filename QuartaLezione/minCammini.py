def bfs(nodo):
    queue = []
    queue.append(nodo)
    queue.append(-1)
    counter = 0
    while len(queue) > 0:
        if nodo == q:
            return counter
        nodo = queue[0]
        if nodo == -1:
            queue.append(-1)
            counter += 1
        if (visited[nodo]):
            queue = queue[1:]
            continue
        for x in graph[nodo]:
            queue.append(x)
        print(nodo, end=' ')
        visited[nodo] = True
        queue = queue[1:]

    return -1

with open("input.txt", 'r') as f:
    lines = f.readlines()

n = int(lines[0].split(' ')[0])
m = int(lines[0].split(' ')[1])
k = int(lines[0].split(' ')[2])
q = int(lines[0].replace("\n", "").split(' ')[3])

graph = [[] for _ in range(n)]
for i in range(m):
    a = int(lines[1+i].split(' ')[0])
    b = int(lines[1+i].replace("\n", "").split(' ')[1])
    graph[a].append(b)
    graph[b].append(a)
print(graph)

visited = [False for _ in range(n)]

risultato = bfs(k)
if (risultato == -1):
    print("\nQ non è raggiungibile partendo da K")
else:
    print("\nQ è raggiungibile partendo da K in " + str(risultato) + " step")
