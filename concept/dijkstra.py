import heapq

# setup data
MAX = 10 ** 10

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# dijsktra
visited = {}
distance = [MAX] * len(graph[0])

queue = [(0, 0)]
distance[0] = 0

while queue:
    w, v = heapq.heappop(queue)

    if v in visited:
        continue

    for vertex in range(0, len(graph[v])):
        if vertex == v or graph[v][vertex] == 0:
            continue

        if graph[v][vertex] + w < distance[vertex]:
            distance[vertex] = graph[v][vertex] + w
            heapq.heappush(queue, (distance[vertex], vertex))

    visited[v] = True
