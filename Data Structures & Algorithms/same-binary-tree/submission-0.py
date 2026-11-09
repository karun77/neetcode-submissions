# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def appendNodesToArray(self,arr,root):
        if root is None:
            arr.append("None")
            return

        arr.append(str(root.val))

        self.appendNodesToArray(arr,root.left)
        self.appendNodesToArray(arr,root.right)

        return

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.appendNodesToArray(arr1,p)
        self.appendNodesToArray(arr2,q)

        return (arr1==arr2)