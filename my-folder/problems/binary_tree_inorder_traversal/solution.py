# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def solve(root):
            if not root:
                return
            solve(root.left)
            lst.append(root.val)
            # solve(root.left)
            solve(root.right)
        solve(root)
        return lst
        