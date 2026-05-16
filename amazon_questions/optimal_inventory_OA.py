# Problem: Amazon OA - Optimal Inventory (getMinAmount)
#
# Given an array of product quality values, convert it to an "optimal inventory"
# where all occurrences of each quality value are contiguous.
#
# Operation: Choose value x, replace ALL occurrences with value y.
# Cost = number of elements changed (count of x in array)
#
# Return the minimum total cost.
#
# Example: [1,2,1,2,1] -> replace all 2s with 1 -> [1,1,1,1,1], cost = 2
#
# Constraints:
# - 1 <= n <= 2*10^5
# - -10^9 <= quality[i] <= 10^9
#
# Approach: Union-Find
# 1. Build distinct sequence (remove consecutive duplicates)
# 2. Union adjacent pairs in distinct sequence
# 3. Each union of two different groups costs 1
# 4. Sum of all union costs = answer

def getMinAmount(quality):
    # Step 1: build distinct sequence
    distinct = []
    for q in quality:
        if not distinct or distinct[-1] != q:
            distinct.append(q)

    # Step 2: union-find with path compression
    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return 1  # new merge, costs 1
        return 0      # already same group, free

    # Step 3: union adjacent pairs and accumulate cost
    cost = 0
    for i in range(len(distinct) - 1):
        cost += union(distinct[i], distinct[i + 1])

    return cost


# --- Tests ---
print(getMinAmount([1, 2, 1, 2, 1]))                          # expected: 2
print(getMinAmount([10, 6, 10, -3, 1, 1, 4, -4, -1, 1, -7])) # expected: 4
print(getMinAmount([7, 2, 5, 7, 3, 5, 3]))                    # expected: 4