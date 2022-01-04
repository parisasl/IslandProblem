class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.bfs(grid, [(i,j)])
                    count += 1
        return count
    
    def bfs(self, grid, coord):
        if len(coord) == 0:
            return
        # the coordinates of the island we are searching on 
        for i, j in coord:
            #print(coord)
            coord.remove((i,j))
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[i]) or grid[i][j] != '1':
                continue
            grid[i][j] = '#'
            # adding the area to the queue
            coord.extend([
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1),
            ])
        self.bfs(grid, coord)
        
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid1))