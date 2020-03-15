from tree import TreeNode
import sys


def is_valid_bst(root: TreeNode):
    stack = []
    t = sys.float_info.min
    while stack or not root:
        while not root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= t:
            return False
        t = root.val
        root = root.right
    return True

