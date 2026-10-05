# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lesser = None
        greater = None
        currentNode = root
        if p.val < q.val:
            lesser = p.val
            greater = q.val
        else:
            lesser = q.val
            greater = p.val

        while(True):
            if (lesser <= currentNode.val) and (greater>=currentNode.val):
                break

            if (lesser < currentNode.val):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right


        return currentNode
        