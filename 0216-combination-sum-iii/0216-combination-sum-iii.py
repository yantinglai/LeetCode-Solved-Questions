class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        total = 0
    
        def backtracking(startIndex, k, n, total):
            if total > n: return 
            if total == n and len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, 10):
                if i in path:
                    continue
                total += i
                path.append(i)
                backtracking(startIndex+1, k, n,total)
                path.pop()
                total -= i
                i += 1    
                
        backtracking(1,k,n,0)
        
        final_res = []
        
        for item in res:
            check = set(item)
            if check not in final_res:
                final_res.append(check)
        return final_res