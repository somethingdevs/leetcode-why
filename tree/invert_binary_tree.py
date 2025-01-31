from typing import Optional

from tree.utils import TreeNode, build_tree_from_list, print_tree, tree_to_list


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)

    return root


tree_values = [4, 2, 7, 1, 3, 6, 9]

# Build tree from list
root = build_tree_from_list(tree_values)

# Print original tree
print("Original tree:")
print_tree(root)

# Invert the tree
inverted_root = invertTree(root)

# Print inverted tree
print("\nInverted tree:")
print_tree(inverted_root)

# Convert to list and print for verification
inverted_list = tree_to_list(inverted_root)
print("\nInverted tree as list:", inverted_list)
