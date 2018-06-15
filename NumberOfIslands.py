class Solution(object):
    rc = 0
    cc = 0
    def isSafe(self, visited, r , c):
        return (r >= 0 and c >= 0 and r < self.rc and c < self.cc and grid[r][c] == 1 and not visited[r][c])


    def dfs(self, visited, r, c):

        rowNbr = [-1, 0, 0,  1]
        colNbr = [0, -1, 1,  0]

        visited[r][c] = True

        for k in xrange(4):
            if self.isSafe(visited, r+rowNbr[k],  c + colNbr[k]):
                self.dfs(visited, r+rowNbr[k], c + colNbr[k])

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.rc = len(grid)
        self.cc = len(grid[0])

        visited = [[False for _ in xrange(self.rc)] for _ in xrange(self.cc)]

        if self.rc == 0 or self.cc == 0:
            return 0
        count = 0
        for i in xrange(self.rc):
            for j in xrange(self.cc):
                if visited[i][j] == False and grid[i][j] == 1:
                    self.dfs(visited, i, j)
                    count += 1
        return count

s =Solution()
grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
print(s.numIslands(grid))