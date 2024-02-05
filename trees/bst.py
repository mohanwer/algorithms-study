class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:

    def __init__(self, root_val: int):
        self.tree = TreeNode(val=root_val)

    def add(self, val: int):
        root = self.tree

        def add_node(node: TreeNode):
            nonlocal val
            if not node:
                return TreeNode(val)
            if node.val > val:
                return add_node(node.left)
            return add_node(node.right)
        
        add_node(root)
        
    def delete(self, key: int):

        root = self.tree

        def successor(node: TreeNode):
            node = node.right
            while node.left:
                node = node.left
            return node
        
        def predecessor(node: TreeNode):
            node = node.left
            while node.right:
                node = node.right
            return node
        
        def delete_node(node: TreeNode, key: int):
            if not node:
                return None
            if node.val > key:
                node.right = delete_node(node.right)
                return node
            if node.val < key:
                node.left = delete_node(node.left)
                return node
            
            if node.right:
                next_node = successor(node)
                node.val = next_node.val
                node.right = delete_node(node.right, next_node.val)
            elif node.left:
                next_node = predecessor(node)
                node.val = next_node.val
                node.left = delete_node(node.left, next_node.val)
            else:
                return None
            return node
        
        delete_node(root, key)
            
