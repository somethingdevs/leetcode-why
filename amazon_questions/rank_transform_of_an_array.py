def arrayRankTransform(arr):
    sorted_arr = sorted(set(arr))

    result = []

    for num in arr:
        for i in range(len(sorted_arr)):
            if sorted_arr[i] == num:
                result.append(i + 1)
                break

    return result


def arrayRankTransformHashMap(arr):
    sorted_arr = sorted(set(arr))

    rank_map = {}
    rank = 1
    for num in sorted_arr:
        rank_map[num] = rank
        rank += 1

    result = []
    for num in arr:
        result.append(rank_map[num])

    return result


arr = [40, 10, 20, 20, 30]
print(arrayRankTransform(arr))
print(arrayRankTransformHashMap(arr))