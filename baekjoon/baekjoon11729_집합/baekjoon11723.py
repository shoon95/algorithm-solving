import sys
sys.stdin = open('input.txt')

N = int(input())

sset = set()

for i in range(N):

    data = input()
    if 'add' in data:
        sset.add(int(data.split()[1]))
    elif 'remove' in data:
        if int(data.split()[1]) in sset:
            sset.remove(int(data.split()[1]))
    elif 'check' in data:
        if int(data.split()[1]) in sset:
            print(1)
        else:
            print(0)
    elif 'toggle' in data:
        if int(data.split()[1]) in sset:
            sset.remove(int(data.split()[1]))
        else:
            sset.add(int(data.split()[1]))
    elif 'all' in data:
        sset = set((range(1,21)))
    elif 'empty' in data:
        sset = set()