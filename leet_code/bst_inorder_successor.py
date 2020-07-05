# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            p = p.right
            while p.left: p = p.left
            return p

        successor = None
        ancestor = root

        while ancestor != p:
            if ancestor.val > p.val:
                successor = ancestor  # we went left, so update the successor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor