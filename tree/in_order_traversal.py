from tree.utils import TreeNode, build_tree_from_list, print_tree


def in_order_traversal(root: TreeNode) -> list[int]:
    # Base case
    if not root:
        return []

    # Recursive case: traverse left subtree, visit root, then traverse right subtree
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)


# Create a binary tree
values = [1, 2, 3, None, 4, None, 5]
root = build_tree_from_list(values)

# Test the in-order traversal
result = in_order_traversal(root)
print("In-order Traversal:", result)
