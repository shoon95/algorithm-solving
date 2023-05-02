import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda n:(n[1], n[0]))

cnt = 1

start = arr[0]
if start[0]==start[1]:
    cnt-=1
for meeting in arr:
    if meeting[0] >= start[1]:
        cnt += 1
        start = meeting
print(cnt)