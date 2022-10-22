class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        used = [0] * len(nums)
        res = []

        def backtracking(nums, used, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for i in range(len(nums)):
                if used[i] == 0:
                    path.append(nums[i])
                    used[i] = 1
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0
        
        backtracking(nums,used,[])
        return res
        