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
        
        def getHeight(root,d):
            if not root: 
                return 0 
            left = getHeight(root.left,d)
            right = getHeight(root.right,d)
            cur_height = max(left,right) + 1
            d[cur_height].append(root.val)
            return cur_height
        
        getHeight(root,d)
        return d.values()
        
        
        
        