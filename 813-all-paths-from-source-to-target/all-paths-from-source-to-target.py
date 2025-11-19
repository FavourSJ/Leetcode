class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []  # Stores all valid paths from source to target
        queue = deque()
        queue.append([0])  # Start with a path containing only the source node (0)

        target = len(graph) - 1  # Target node is the last node

        # Process the queue until no paths are left
        while queue:
            path = queue.popleft()  # Get the next path to explore
            last_node = path[-1]    # Current node is the last element in the path

            # If last node is the target, add the path to the results
            if last_node == target:
                res.append(path)
                continue  # No need to explore further from the target

            # Otherwise, extend the path to all neighbors of the last node
            for nei in graph[last_node]:
                # Create a new path by appending the neighbor
                # This ensures original path is not modified (important for other branches)
                new_path = path + [nei]
                queue.append(new_path)  # Add the new path to the queue for further exploration

        return res  # Return all found paths