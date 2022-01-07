class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
                
        for y in range(m):
            for x in range(n):
                
                if x > 0:
                    dp[y][x] += dp[y][x-1]
                
                if y > 0:
                    dp[y][x] += dp[y-1][x]
                
        return dp[m-1][n-1]
                