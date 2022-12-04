
def read_file():
    return open('adv03-2022.txt', 'r').read().split('\n')

def part1():
    sum = 0
    data=read_file()
    for rucksack in data:
        letter=''.join([*set([letter for letter in rucksack[:int(len(rucksack)/2)] if letter in rucksack[int(len(rucksack)/2):]])])
        sum+=ord(letter) - (38 if letter.isupper() else 96)
    print(f'Part 1 value: {sum}')

def part2():
    data=read_file()
    l=[]
    sum=0
    groups=[data[i:i+3] for i in range(0, len(data), 3)]
    for group in groups:
        letter=''.join(set.intersection(set(group[0]), set(group[1]), set(group[2])))
        sum+=ord(letter) - (38 if letter.isupper() else 96)
    print(f'Part 1 value: {sum}')

if __name__ == '__main__':
    part1()
    # part2()