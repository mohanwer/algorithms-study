from typing import List

from leet_code.binary_tree_inorder_traversal import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(root.right)
        return res[::-1]