import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())

price_all = [0] + list(map(int, input().split()))
arr = [[0] for _ in range(N+1)]
visit = [0] * (N+1)

def dfs(start):
    global min
    global all
    all.append(start)
    stack = [start]

    while stack:
        value = stack.pop()
        if price_all[value] < min:
            min = price_all[value]

        for j in arr[value]:
            if visit[j] != 1:
                visit[j] = 1
                stack.append(j)
                all.append(j)


for _ in range(M):
    f1, f2 = map(int, input().split())
    if arr[f1] == [0]:
        arr[f1] = [f2]
    else:
        arr[f1].append(f2)
    if arr[f2] ==[0]:
        arr[f2] = [f1]
    else:
        arr[f2].append(f1)

price = 0
all = []

for i in range(1,N+1):
    if visit[i] != 1 and arr[i] != [0] and price_all[i] + price<=K:
        visit[i] = 1
        min = price_all[i]
        dfs(i)
        price += min

for i in range(1,N+1):
    if i not in all:
        price += price_all[i]

if price <= K :
    print(price)
else:
    print("Oh no")

