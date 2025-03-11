class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color of the starting pixel
        start_color = image[sr][sc]

        # If the new color is the same as the current color, no changes needed
        if start_color == color:
            return image

        def dfs(r: int, c: int):
            # Base Case: Stop if out of bounds or if the color is different from the original
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != start_color:
                return

            # Change the current pixel's color
            image[r][c] = color

            # Recursively call DFS in all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Start the flood fill
        dfs(sr, sc)

        return image
        