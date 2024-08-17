# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node, result):
            if not node: return 0

            result = 2 * result + node.val

            if not node.left and not node.right:
                return result
            return helper(node.left, result) + helper(node.right, result)
        return helper(root, 0)

        