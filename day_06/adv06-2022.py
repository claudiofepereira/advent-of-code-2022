
def read_file():
    return open('adv06-2022.txt', 'r').read().split('\n')

def main(c='', s=0):
    data = read_file()[0]
    l = len(data)
    for i in range(0, l, 1):
        n = data[i:i+s]
        if len(set(n)) == s:
            c=n, i+s
            break
    print(f'Value: {c}')

if __name__ == '__main__':
    main(s=4)
    main(s=14)
