class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        total = 0
    
        def backtracking(startIndex, k, n, total):
            if total > n: return 
            if len(path) == k and total == n:
                    res.append(path[:])
                    return
            for i in range(startIndex, 10 - (k-len(path))+1):
                total += i
                path.append(i)
                backtracking(startIndex+1, k, n,total)
                path.pop()
                total -= i 
                startIndex += 1
                
        backtracking(1,k,n,0)
#         final_res = []
        
#         for item in res:
#             check = set(item)
#             if check not in final_res:
#                 final_res.append(check)
        return res