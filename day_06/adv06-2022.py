
def read_file():
    return open('adv06-2022.txt', 'r').read().split('\n')


def part1(c=''):
    data = read_file()[0]
    for i in range(0, len(data), 1):
        n = data[i:i+4]
        if len(set(n)) == len(n):
            c=n, i+4
            break
    print(f'Part 1 value: {c}')


def part2(c=''):
    data = read_file()[0]
    for i in range(0, len(data), 1):
        n = data[i:i+14]
        if len(set(n)) == len(n):
            c=n, i+14
            break
    print(f'Part 2 value: {c}')


if __name__ == '__main__':
    part1()
    part2()
