# Leetcode: https://leetcode.com/problems/all-paths-from-source-to-target/

def allPathsSourceTarget(graph):
    if len(graph) == 0:
        return []
    
    def search(graph, fr, to, path, solution):
        if fr == to:
            solution.append([] + path)
            return
        
        for node in graph[fr]:
            path.append(node)
            search(graph, node, to, path, solution)
            path.pop()
    
    solution = []
    search(graph, 0, len(graph) - 1, [0], solution)

    return solution


if __name__ == '__main__':
    assert allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
    assert allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
