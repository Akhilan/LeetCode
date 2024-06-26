# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        def dfs(node, h, dr):
            
            if h == d:
                tmp = TreeNode(v)
                #if not node: return tmp
                if dr == 0:
                    tmp.left = node
                else:
                    tmp.right = node
                return tmp
            
            if not node: return node
            
            node.left = dfs(node.left, h+1, 0)
            node.right = dfs(node.right, h+1, 1)
            return node
            
        return dfs(root, 1, 0)