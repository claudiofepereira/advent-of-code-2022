import re

data = open("adv07-2022.txt").read().splitlines()

navigate_down = "cd ([A-Za-z0-9]+)"
navigate_up = "cd \.\."
file_size = "([0-9]+) (?:[A-Za-z0-9]+)"

folders = dict()
current_dir = [""]

for row in data:
    if re.search(navigate_up, row):
        current_dir.pop()
    elif re.search(navigate_down, row):
        current_dir.append(re.findall(navigate_down, row)[0])
    elif re.search(file_size, row):
        next_size = int(re.findall(file_size, row)[0])
        path = ""
        for dir in current_dir:
            path += "/" + dir
            if not path in folders:
                folders[path] = 0
            folders[path] += next_size


# part 1
# Loop through all the directories and discard the ones above 100000 in size.
# Then sum the values of the remainding directories.
MAX_SIZE = 100000
print(sum(filter(lambda size: size <= MAX_SIZE, map(lambda file: folders[file], folders))))

# part 2
# Get the remainding size needed to be freed up in order to update the system.
# subtract the root folder size and add the free space needed.
space_to_free = folders["/"] - 70000000 + 30000000
print(min(list(filter(lambda size: size > space_to_free, map(lambda path: folders[path], folders)))))
