class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append([0])  # Start with path containing source node

        target = len(graph) - 1

        while queue:
            path = queue.popleft()
            last_node = path[-1]

            if last_node == target:
                res.append(path)
                continue

            for nei in graph[last_node]:
                queue.append(path + [nei])  # Extend path with neighbor

        return res