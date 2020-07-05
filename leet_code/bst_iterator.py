# https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/1008/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        prev = None
        node = self.root
        while node.left:
            prev = node
            node = node.left
        v = node.val
        if node.right and prev:
            if node != self.root:
                prev.left = node.right
        elif prev:
            prev.left = None
        else:
            self.root = self.right
        return v

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.root.left is not None or self.root.right is not None
