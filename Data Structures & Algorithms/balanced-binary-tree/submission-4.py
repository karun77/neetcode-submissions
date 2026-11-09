# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, depth, root: Optional[TreeNode]):
        if root==None:
            return depth
        leftDepth=depth
        if root.left!=None:
            leftDepth=self.maxDepth(1+depth,root.left)
        rightDepth=depth
        if root.right!=None:
            rightDepth=self.maxDepth(1+depth,root.right)

        if leftDepth==-1:
            return -1
        if rightDepth==-1:
            return -1

        if(abs(leftDepth-rightDepth)>1):
            return -1
        else:
            return max(leftDepth,rightDepth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        
        if self.maxDepth(1,root)==-1:
            return False

        if abs(self.maxDepth(1,root.left)-self.maxDepth(1,root.right))<=1:
            return True
        
        return False
        