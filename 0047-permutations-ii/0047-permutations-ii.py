class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = [0] * len(nums)
        nums.sort() 
        
        def backtracking(used, nums, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 

            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    path.append(nums[i])
                    used[i] = 1
                    backtracking(used, nums, path)
                    path.pop()
                    used[i] = 0
                    
        backtracking(used, nums, [])
        return res