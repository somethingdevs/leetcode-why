def maxBottlesDrunk(numBottles: int, numExchange: int) -> int:
    total_drunk = 0
    empty_bottles = 0

    while numBottles > 0:
        total_drunk += numBottles
        empty_bottles += numBottles
        numBottles = 0

        while empty_bottles >= numExchange:
            numBottles += 1
            empty_bottles = empty_bottles - numExchange
            numExchange += 1

    return total_drunk


print(maxBottlesDrunk(10, 3))
