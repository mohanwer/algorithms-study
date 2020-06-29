# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        items = []
        stack = deque()
        while True:
            if root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                return items
            if root is None:
                node = stack.pop()
                items.append(node.val)
                root = node.right
