class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # store all valid paths from source to target
        res = []
        queue = deque()
        # start with a path containing only the source node
        queue.append([0])
        # target node is the last one
        target = len(graph) - 1

        # process through the queue until no paths are left
        while queue:
            # get the next path to explore
            path = queue.popleft()
            # current node is the last element in the path
            last_node = path[-1]

            # if the last node is the target and the path to the results
            if last_node == target:
                res.append(path)
                continue

            # otherwise extend the path to all neighbours of the last node
            for nei in graph[last_node]:
                # create a new path appending it to the neigbour
                # this ensures the original path is not modified
                new_path = path + [nei]
                queue.append(new_path)

        return res
