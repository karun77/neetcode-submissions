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
 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            if subRoot is None:
                return True
            return False

        arr1 = []
        self.appendNodesToArray(arr1,root)

        arr2=[]
        self.appendNodesToArray(arr2,subRoot)

        if arr1==arr2:
            return True

        if self.isSubtree(root.left,subRoot):
            return True

        if self.isSubtree(root.right,subRoot):
            return True

        return False




        