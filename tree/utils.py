class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values):
    """
    Build a binary tree from a list of values.
    Use 'None' to indicate missing nodes.
    """
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_to_list(root):
    """
    Convert a binary tree to a list of values (level-order traversal).
    Use 'None' for missing nodes.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for a cleaner representation
    while result and result[-1] is None:
        result.pop()
    return result


def print_tree(root, level=0, prefix="Root:"):
    """
    Print a binary tree in a human-readable format.
    """
    if not root:
        print(" " * (level * 4) + prefix + " None")
        return
    print(" " * (level * 4) + prefix + f" {root.val}")
    if root.left or root.right:
        print_tree(root.left, level + 1, "L---")
        print_tree(root.right, level + 1, "R---")
