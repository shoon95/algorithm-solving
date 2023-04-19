import sys
sys.stdin = open('input.txt')

d = [(-1,0),(1,0), (0, -1), (0, 1)]

M, N, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            maps[y][x] = 9999

check = {}

def bfs(start_row, start_col, cnt):
    queue = []
    maps[start_row][start_col] = cnt 
    queue.append([start_row, start_col])
    check[cnt] = 1
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r+d[i][0]
            nc = c+d[i][1]
            if 0 <= nr < M and 0 <= nc  < N and maps[nr][nc] == 0:
                maps[nr][nc] = cnt
                queue.append([nr, nc])
                check[cnt] += 1
cnt = 1
for r in range(M):
    for c in range(N):
        if maps[r][c] == 0:
            bfs(r, c, cnt)
            cnt += 1

result = [i[1] for i in sorted(list(check.items()), key=lambda n:n[1])]
print(len(result))
for i in result:
    print(i, end=' ')