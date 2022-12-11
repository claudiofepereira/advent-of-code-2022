input = open('adv10-2022.txt', 'r').read().split('\n')

d = {}
cycles = 0
tot = 1

for line in input:
    move = line.split(' ')
    cycles += 2 if move[0] == 'addx' else 1
    tot += int(move[1]) if len(move) == 2 else 0
    # print(cycles, int(move[1]) if len(move) == 2 else 0, tot)
    d[str(cycles)] = [move[0], tot]

r = 0
for i in range(20, cycles, 40):
    for x in range(1,3):
        key = str(i-x)
        if key in d:
            r +=  i * d[key][1]
            break
print(f'Part 1 value: {r}')

crt = ''
crt_cycle = 0
dict_length = int(list(d)[-1])
for i in range(dict_length):
    # Update the sprite position if there's a change in the X register.
    key = str(i)
    if i % 40 == 0:
        crt_cycle = i
        sprite_pos = [0, 1, 2]
    c = i - crt_cycle
    if key in d:
        x_reg = d[key][1]
        sprite_pos = [x_reg-1, x_reg, x_reg+1]
    if c in sprite_pos:
        crt += '#'
    else:
        crt += '.'

print('Part 2 value:')
for i in range(int(len(crt)/40)):
    print(crt[40*i:40*(i+1)])