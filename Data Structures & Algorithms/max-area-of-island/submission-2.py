class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid),len(grid[0])

        def dfs(r, c):
            nonlocal res, best
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return

            grid[r][c] = 0
            res += 1 
            best = max(res, best)
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = 0
                    dfs(r, c)
                    
        return best
