class Graph:
    def __init__(self):
        self.adjacency = {}

    def connect(self, src, dst, weight):
        self.adjacency[src] = self.adjacency.get(src, {})
        self.adjacency[src][dst] = weight


def shortest_path(g: Graph, src, dst, visited={}, memo={}):
    min_distance = 2 ** 10

    if (src, dst) in memo:
        return memo[(src, dst)]
    
    if src == dst:
        return 0

    for node in g.adjacency.get(src, {}):
        if node in visited:
            continue

        min_distance = min(
            min_distance, 
            g.adjacency[src][node] + shortest_path(g, node, dst, {**visited, src: True, node: True}, memo))

    memo[(src, dst)] = min_distance

    return memo[(src, dst)]


if __name__ == '__main__':
    g = Graph()
    g.connect('A', 'B', 4)
    g.connect('A', 'C', 2)
    g.connect('B', 'C', 5)
    g.connect('B', 'D', 10)
    g.connect('C', 'E', 3)
    g.connect('D', 'F', 11)
    g.connect('D', 'A', 7)
    g.connect('E', 'D', 4)
    assert shortest_path(g, 'A', 'F') == 20
