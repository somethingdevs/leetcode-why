def getJSONDiff(json1, json2):
    result = []
    for index, n in enumerate(json1):
        print(n)
        if json1[n] != json2[n]:
            result.append(n)

    return sorted(result)


print(getJSONDiff({'hacker': 'rank', 'input': 'output'}, {'hacker': 'ranked', 'input': 'wrong'}))
