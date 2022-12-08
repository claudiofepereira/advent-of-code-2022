import re

stacks = []

find_numbers = "([0-9]+)"

data = open('adv05-2022.txt', 'r')

# Get the stacks in a list of lists format.
for line in data:
    if line == '\n': break
    stacks.append([line[k*4+1] for k in range(len(line) // 4)])

# Remove the last list, since it's the indexes of the stacks.
stacks.pop()

# Remove empty containers, invert the columns and return as list of lists again.
stacks = ([list(''.join(col).strip()[::-1]) for col in zip(*stacks)])

# for line in data:
#     a,b,c = map(int,(re.findall(find_numbers, line)))
#     stacks[c-1].extend(stacks[b-1][-a:][::-1])
#     stacks[b-1] = stacks[b-1][:-a]
# print('Part 1 result:',''.join([r[-1] for r in stacks]))

for line in data:
    a,b,c = map(int,(re.findall(find_numbers, line)))
    stacks[c-1].extend(stacks[b-1][-a:])
    stacks[b-1] = stacks[b-1][:-a]
print('Part 2 result:',''.join([r[-1] for r in stacks]))

