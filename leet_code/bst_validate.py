class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:

    def isValid(root, small, lrg):
        if root is None:
            return True
        if not small < root.val < lrg:
            return False

        small = min(small, root.val)
        lrg = max(lrg, root.val)

        return isValid(root.right, small, float('inf')) and isValid(root.left, float('-inf'), lrg)