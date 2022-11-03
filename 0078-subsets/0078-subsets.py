class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def backtracking(nums, startIndex,path):
            if path in res:
                return
            res.append(path.copy())
            if startIndex == len(nums):
                return 
            
            for i in range(startIndex, len(nums)):
                path.append(nums[i])   
                backtracking(nums, i+1,path)
                path.pop()
                backtracking(nums, startIndex+1, path)
        
        backtracking(nums,0,[])
        return res
                    