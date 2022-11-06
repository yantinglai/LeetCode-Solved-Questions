import numpy as np
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # try to calculate the longest path for each point and add it up 
        # can use a dp array to store the value 
        m = len(matrix)
        n = len(matrix[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        # print(dp)
    
        def dfs(r,c,prev_val):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] <= prev_val:
                return 0
            if dp[r][c] != 1:  # if it is already visited, return this value
                return dp[r][c] # where do you initialize the res?
            
            res = 1
            res = max(res, dfs(r+1,c,matrix[r][c]) + 1)
            res = max(res, dfs(r-1,c,matrix[r][c]) + 1)
            res = max(res, dfs(r,c+1,matrix[r][c]) + 1)
            res = max(res, dfs(r,c-1,matrix[r][c]) + 1)
            
            dp[r][c] = res
            return res
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,-1)  # prev_val set as -1 
        return np.max(dp) 
    
        
    