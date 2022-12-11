input = open('adv10-2022.txt', 'r').read().split('\n')

d = {}
cycles = 0
tot = 1

for line in input:
    move = line.split(' ')
    # Add 2 to cycles if move is 'addx', otherwise add 1
    cycles += 2 if move[0] == 'addx' else 1
    # Increment tot by the second value in the move list, if present
    tot += int(move[1]) if len(move) == 2 else 0
    d[cycles] = [move[0], tot]

r = 0
for i in range(20, cycles, 40):
    for x in range(1,3):
        key = i-x
        if key in d:
            r +=  i * d[key][1]
            break
print(f'Part 1 value: {r}')

crt = ''
crt_cycle = 0
dict_length = list(d)[-1]
for i in range(dict_length):
    # Update the sprite position if there's a change in the X register.
    key = i
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
# Iterate over the crt string in steps of 40
for i in range(0, len(crt), 40):
    # Concatenate the substring of crt starting at index i and
    # ending at index i+40 with a newline character and print the result
    print(''.join(crt[i:i+40]))

