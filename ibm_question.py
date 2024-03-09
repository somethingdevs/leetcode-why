def get_potential_of_winner(potential: list, k: int):
    max_potential = 0

    for i in range(len(potential)):
        if potential[i] > potential[i + 1]:
            max_potential += 1
            temp = potential[i + 1]
            potential.remove(potential[i + 1])
            potential.append(temp)

        else:
            max_potential = 0
            temp = potential[i]
            potential.remove(potential[i])
            potential.append(temp)

        if max_potential == 2:
            return potential[i]


def rolling_string(s, operations):
    pass



# get_potential_of_winner([3, 2, 1, 4], 2)
rolling_string('abc', ['0 0 L', '2 2 L', '0 2 R'])