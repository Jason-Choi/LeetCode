class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
                
        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 1:
                    continue
                if x > 0:
                    dp[y][x] += dp[y][x-1]
                
                if y > 0:
                    dp[y][x] += dp[y-1][x]
                
        return dp[m-1][n-1]
                 