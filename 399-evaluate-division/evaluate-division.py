class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build adjacency list: each variable maps to neighbours and thei rratip
        adj = collections.defaultdict(list)

        for i, (a, b) in enumerate(equations):
            # a to b with weight value
            adj[a].append([b, values[i]])
            # b to a with reciprocal weighted value
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            # if either variable doesn't exist, no valid ratio
            if src not in adj or target not in adj:
                return -1.0

            # BFS: track node and accumulated product
            q = deque([(src, 1.0)])
            visited = set([src])

            while q:
                node, ratio = q.popleft()

                # found the target, current ratio is the answer
                if node == target:
                    return ratio

                # go through neighours, multiplying through the weights
                for nei, weight in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, ratio * weight))

            # no path
            return -1.0

        # evaluate all queries using BFS
        return [bfs(x, y) for x, y in queries]