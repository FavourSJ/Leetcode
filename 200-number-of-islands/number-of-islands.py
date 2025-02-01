# Graph traversal algorithm from the original point and iterating through

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 # counter to keep track of the islands found
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c): #Function -> Breadth-First Search (BFS) to explore and mark all cells of the island
            q = deque() # que to process cells and pop from the front
            q.append((r, c)) # add starting cell to the que
            grid[r][c] = "0"

            # while loop to process every cell till the end
            while q: 
                row, col = q.popleft() # dequeue the front cell
                directions = [[1,0],[-1,0],[0,1],[0,-1]] # four possible movements (vector)

                for dr, dc in directions: # iterates through each direction
                    r, c = row + dr, col + dc # compute the new cells coordinates
                    # ensure the new cell is within boundary
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                        # if TRUE add the new cell to the que and mark as visited
                        q.append((r, c)) 
                        grid[r][c] = "0"
       
        for r in range(rows): # loop through each row
            for c in range(cols): # loop through each column in the current row
                if grid[r][c] == "1": # check if cell is an island and not visited
                    # if TRUE add 1 to the island counter
                    islands = islands + 1
                    # call bfs to mark all connected land cells of this island
                    bfs(r, c)

        return islands