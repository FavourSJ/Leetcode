# Graph traversal algorithm from the original point and iterating through

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        # dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            # store the cells to be processed in a queue
            q = deque()
            # start BFS from the given land cell
            q.append((r,c))
            # mark the starting cell as visited
            grid[r][c] = "0"

            # define directions of possible movement (up, down, left, right)
            directions = [
                [1,0],
                [-1,0],
                [0,1],
                [0,-1]
            ]

            # start processing the cells in the queue
            # so while we "have cells"
            while q:
                row, col = q.popleft()

                # explore the four directions
                for dr, dc in directions:
                    # find the new cell coordinates
                    new_r, new_c = row + dr, col + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        # add new cell to the queue
                        q.append((new_r, new_c))
                        # mark as visited
                        grid[new_r][new_c] = "0"

        # iterate through the rest of the cells in the grid
        for r in range(rows):
            for c in range(cols):
                # if the cell is '1', then we have found a new island!
                if grid[r][c] == "1":
                    # add 1 to the number of islands
                    islands += 1
                    # call bfs to mark the connected islands
                    bfs(r, c)

        return islands
