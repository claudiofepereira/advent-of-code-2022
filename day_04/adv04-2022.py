
def read_file():
    return open('adv04-2022.txt', 'r').read().split('\n')

def part1():
    c = 0
    groups = [g.split(',')[0].split('-')+g.split(',')[1].split('-') for g in read_file()]
    x = [[int(j) for j in i] for i in groups]
    for g in x:
        if (g[0] <= g[2] and g[1] >= g[3]) or (g[2] <= g[0] and g[3] >= g[1]):
            c+=1
    print(f'Part 1 value: {c}')

def part2():
    c = 0
    groups = [g.split(',')[0].split('-')+g.split(',')[1].split('-') for g in read_file()]
    x = [[int(j) for j in i] for i in groups]
    for g in x:
        if (
            ((g[2] <= g[0] <= g[3]) or (g[2] <= g[1] <= g[3]))
            or 
            ((g[0] <= g[2] <= g[1]) or (g[0] <= g[3] <= g[1]))
        ):
            c+=1
    print(f'Part 2 value: {c}')


if __name__ == '__main__':
    part1()
    part2()