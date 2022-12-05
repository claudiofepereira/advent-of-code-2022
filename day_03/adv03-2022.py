
def read_file():
    return open('adv03-2022.txt', 'r').read().split('\n')

def part1():
    t = 0
    for rucksack in read_file():
        letter=''.join([*set([letter for letter in rucksack[:int(len(rucksack)/2)] if letter in rucksack[int(len(rucksack)/2):]])])
        t+=ord(letter) - (38 if letter.isupper() else 96)
    print(f'Part 1 value: {t}')

def part2():
    t=0
    groups=[read_file()[i:i+3] for i in range(0, len(read_file()), 3)]
    for group in groups:
        letter=''.join(set.intersection(set(group[0]), set(group[1]), set(group[2])))
        t+=ord(letter) - (38 if letter.isupper() else 96)
    print(f'Part 2 value: {t}')

if __name__ == '__main__':
    part1()
    part2()