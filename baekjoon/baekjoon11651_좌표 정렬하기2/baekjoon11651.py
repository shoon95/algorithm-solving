import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))

arr.sort(key = lambda  n : (n[1],n[0])) # x 기준, y 기준 순으로 정렬한다
for i in arr:
    print(*i)