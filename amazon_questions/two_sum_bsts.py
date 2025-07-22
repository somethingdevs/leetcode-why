class Solution:
    def findTarget(self, root, k):
        # Step 1: In-order traversal to get sorted values
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)

        # Step 2: Two-pointer approach
        left, right = 0, len(values) - 1
        while left < right:
            current_sum = values[left] + values[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return False
