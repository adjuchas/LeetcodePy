from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def getlis(root: TreeNode, lis: List[int]) -> None:
        if root is None:
            return None
        Solution.getlis(root.left, lis)
        lis.append(int(root.val))
        Solution.getlis(root.right, lis)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis1 = []
        Solution.getlis(root, lis1)
        return lis1
