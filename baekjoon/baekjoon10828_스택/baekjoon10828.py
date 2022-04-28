import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def stack(data):
    if 'top' in data:
        if len(arr) !=0:
            return(arr[-1])
        else:
            return(-1)
    elif 'size' in data:
        return(len(arr))
    elif 'pop' in data:
        if len(arr)==0:
            return(-1)
        else:
            return(arr.pop())
    else:
        if len(arr) == 0:
            return(1)
        else:
            return(0)

N = int(input())

arr = []
for _ in range(N):
    data = input()
    if 'push' in data:
        arr.append(data.split()[1])
    else:
        print(stack(data))