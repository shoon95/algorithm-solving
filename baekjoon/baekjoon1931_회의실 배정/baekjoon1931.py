import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda n:n[1])
print(arr)
cnt = 1

start_meeting = arr[0]
for meeting in arr:
    if meeting[0] > start_meeting[1]:
        cnt += 1
        start_meeting = meeting

print(cnt)