class Solution(object):
    def helper(self, grid, visited, r, c):
        if r < 0 or c < 0 or r >= len(visited) or c >= len(visited[0]):
            return
        if visited[r][c] == True:
            return
        visited[r][c] = True
        if grid[r][c] == '0':
            return
        else:
            self.helper(grid, visited, r + 1, c)
            self.helper(grid, visited, r - 1, c)
            self.helper(grid, visited, r, c + 1)
            self.helper(grid, visited, r, c - 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rc = len(grid)
        if rc == 0:
            return 0
        cc = len(grid[0])

        visited = [[False for _ in xrange(cc)] for _ in xrange(rc)]

        for i in xrange(rc):
            for j in xrange(cc):
                if not visited[i][j] and grid[i][j] == '1':
                    self.helper(grid, visited, i, j)
                    count += 1
        return count

s = Solution()
inp=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
res = s.numIslands(inp)
print(res)