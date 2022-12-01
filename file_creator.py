import os

type_files = ['py', 'txt']

for i in range(1,26):
    if not os.path.isdir(f'./day-{i}'):
        print('Directory ./day-{i} did not exist. Creating it now.')
        os.mkdir(f'./day-{i}')
    for type in type_files:
        if not os.path.exists(f'./day-{i}/adv{i}-2022.{type}'):
            print(f"file ./day-{i}/adv{i}-2022.{type} did not exist. Creating it now.")
            with open(f'./day-{i}/adv{i}-2022.{type}','w') as f:
                f.write('')