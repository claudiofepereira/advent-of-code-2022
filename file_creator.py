import os

type_files = ['py', 'txt']

for i in range(1,26):
    i = str(i).zfill(2)
    if not os.path.isdir(f'./day_{i}'):
        print(f'Directory ./day_{i} did not exist. Creating it now.')
        os.mkdir(f'./day_{i}')
    for type in type_files:
        if not os.path.exists(f'./day_{i}/adv{i}-2022.{type}'):
            print(f"file ./day_{i}/adv{i}-2022.{type} did not exist. Creating it now.")
            with open(f'./day_{i}/adv{i}-2022.{type}','w') as f:
                f.write('')