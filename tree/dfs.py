from tree.utils import TreeNode, build_tree_from_list, print_tree


def dfs(root: TreeNode) -> list[int]:
    stack = [root]
    result = []
    
    if not root:
        return []

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


# Example tree: [1, 2, 3, None, 5, 6, 7]
values = [1, 2, 3, None, 5, 6, 7]

# Build tree from list
root = build_tree_from_list(values)

# Print the tree structure
print("Binary Tree Structure:")
print_tree(root)

# Perform DFS traversal
dfs_result = dfs(root)

# Print the DFS output
print("\nDFS Traversal (Preorder):", dfs_result)
