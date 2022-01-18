class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return
            
            grid[i][j] = "-1"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island_count += 1
                    
                    
        return island_count
