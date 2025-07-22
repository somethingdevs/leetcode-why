from tree.utils import TreeNode, build_tree_from_list, print_tree


def bfs(root: TreeNode) -> list[int]:
    result = []
    if not root:
        return []

    current = root
    bfs_queue = []

    while current:
        current = bfs_queue.pop()
        result.append(current)
        bfs_queue.append(current.left)
        bfs_queue.append(current.right)
    return result


# Example tree: [1, 2, 3, None, 5, 6, 7]
values = [1, 2, 3, None, 5, 6, 7]

# Build tree from list
root = build_tree_from_list(values)

# Print the tree structure
print("Binary Tree Structure:")
print_tree(root)

# Perform DFS traversal
bfs_result = bfs(root)

# Print the DFS output
print("\nBFS Traversal (Preorder):", bfs_result)
