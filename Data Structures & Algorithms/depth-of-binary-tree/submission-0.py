# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        level=1 #just by coming to this node we have advanced down by 1
        leftSum=0
        if root.left!=None:
            leftSum=self.maxDepth(root.left)

        rightSum=0
        if root.right!=None:
            rightSum=self.maxDepth(root.right)

        return level+max(leftSum,rightSum)