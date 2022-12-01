
def main():
    l = []
    data = open('adv1-2022.txt', 'r')
    elfs = data.read().strip().split('\n\n')
    for meals in elfs:
        sum_l = sum([int(num) for num in meals.split('\n')])
        l.append(sum_l)
    print(f'Part 1 value: {max(l)}')
    print(f'Part 2 value: {sum(sorted(l)[len(l)-3:])}')

if __name__ == '__main__':
    main()