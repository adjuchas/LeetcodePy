from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getlist(root: TreeNode, lis:List[int]) -> List[int]:
        if root is None:
            return None
        getlist(root.left, lis)
        lis.append(int(root.val))
        getlist(root.right, lis)
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lis1 = []
        lis2 = []
        getlist(root1, lis1)
        getlist(root2, lis2)
        for i in lis2:
            lis1.append(i)
        lis1.sort()
        return lis1