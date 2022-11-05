# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         1: 3,4,5
#         2: 2 
#         3: 1
        
        d = collections.defaultdict(list)
        
        def getHeight(root):
            if not root: 
                return 0 
            left = getHeight(root.left)
            right = getHeight(root.right)
            cur_height = max(left,right) + 1
            d[cur_height].append(root.val)
            print(d)
            return cur_height
        
        getHeight(root)
        return d.values()
        
        # 1: left. :2  right: 1 - max(2,1) -- 2+1     
        # 2: left = 1.   right = 1   
        # 4: left = 0 , right =0  -- 1 
        # 5: left = 0 , right =0 --- 1
        # 3: left = 0, right =0 --- 1
        
        
        