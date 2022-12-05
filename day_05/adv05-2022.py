
def read_file():
    return open('adv05-2022.txt', 'r').read().split('\n\n')


def part1(c=''):
    data = read_file()
    arr = []
    stacks, moves = data[0], data[1]
    # Processing the number of stacks to consider into a dictionary.
    dict_stacks = {key: [] for key in stacks.split(
        '\n')[len(stacks.split('\n'))-1:][0].split(' ') if key != ''}
    # Processing the containers inside the stacks.
    for i in stacks.split('\n')[:len(stacks.split('\n'))-1]:
        aux = []
        cont = 0
        for x in i.split(' '):
            if cont == 4:
                aux.append(None)
                cont = 0
            if x != '':
                aux.append(x.replace('[', '').replace(']', ''))
                cont = 1
            else:
                cont += 1
        arr.append(aux)
    # Stacks separated by column number.
    for key in dict_stacks.keys():
        dict_stacks[key].append([i[int(key)-1]
                                for i in arr if i[int(key)-1] != None])
        dict_stacks[key][0].reverse()
    # Movement time.
    for move in moves.split('\n'):
        n = [int(x) for x in move.split() if x.isdigit()]
        # Move n[0] containers from n[1] to n[2]
        # First add to the stack that is receiving containers in reverse order.
        dict_stacks[str(n[2])][0] += dict_stacks[str(n[1])][0][:-n[0]-1:-1]
        # Remove from the stack that got containers removed.
        dict_stacks[str(n[1])][0] = dict_stacks[str(n[1])][0][slice(
            0,
            len(dict_stacks[str(n[1])][0])-n[0])]
    res = [dict_stacks[key][0][-1] for key in dict_stacks.keys()]
    for letter in res:
        c += letter
    print(f'Part 1 value: {c}')


def part2(c=''):
    data = read_file()
    arr = []
    stacks, moves = data[0], data[1]
    # Processing the number of stacks to consider into a dictionary.
    dict_stacks = {key: [] for key in stacks.split(
        '\n')[len(stacks.split('\n'))-1:][0].split(' ') if key != ''}
    # Processing the containers inside the stacks.
    for i in stacks.split('\n')[:len(stacks.split('\n'))-1]:
        aux = []
        cont = 0
        for x in i.split(' '):
            if cont == 4:
                aux.append(None)
                cont = 0
            if x != '':
                aux.append(x.replace('[', '').replace(']', ''))
                cont = 1
            else:
                cont += 1
        arr.append(aux)
    # Stacks separated by column number.
    for key in dict_stacks.keys():
        dict_stacks[key].append([i[int(key)-1]
                                for i in arr if i[int(key)-1] != None])
        dict_stacks[key][0].reverse()
    # Movement time.
    for move in moves.split('\n'):
        n = [int(x) for x in move.split() if x.isdigit()]
        # Move n[0] containers from n[1] to n[2]
        # First add to the stack that is receiving containers.
        dict_stacks[str(n[2])][0] += dict_stacks[str(n[1])][0][-n[0]:]
        # Remove from the stack that got containers removed.
        dict_stacks[str(n[1])][0] = dict_stacks[str(n[1])][0][slice(
            0,
            len(dict_stacks[str(n[1])][0])-n[0])]
    res = [dict_stacks[key][0][-1] for key in dict_stacks.keys()]
    for letter in res:
        c += letter
    print(f'Part 2 value: {c}')


if __name__ == '__main__':
    part1()
    part2()
