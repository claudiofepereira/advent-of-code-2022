
def read_file():
    return open('adv05-2022.txt', 'r').read().split('\n\n')

def part1(c=''):
    data = read_file()
    arr = []
    stacks, moves = data[0], data[1]
    # Processing the number of stacks to consider into a dictionary.
    dict_stacks = dict.fromkeys([i for i in stacks.split('\n')[len(stacks.split('\n'))-1:][0].split(' ') if i != ''], [])
    # Processing the containers inside the stacks.
    for i in stacks.split('\n')[:len(stacks.split('\n'))-1]:
        aux = []
        cont = 0
        for x in i.split(' '):
            if cont == 4:
                aux.append(None)
                cont = 0
            if x != '':
                aux.append(x.replace('[','').replace(']','')) 
                cont = 1
            else:
                cont+=1
        arr.append(aux)
    print(arr)
    for s in arr:
        print(s)
        for idx, i in enumerate(s):
            print(idx, i)
            dict_stacks[str(idx+1)].append(i)
    print(dict_stacks)


def part2(c=''):
    print(f'Part 2 value: {c}')

if __name__ == '__main__':
    part1()
    # part2()
