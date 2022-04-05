import sys
from pprint import pprint
sys.stdin = open('input.txt')

'''
결국은  다 돌면서 최소 값으로 해당 칸을 업데이트해주고, 다음 칸이 지금 나보다 더 작다면 더이상 돌지 않는다.
'''
d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start):
    Q = [start]
    maps[start[0]][start[1]] = 0
    while Q:
        v = Q.pop(0)
        if v[0] ==N-1 and v[1] == N-1:
            continue
        for i in range(4):
            nr = v[0] + d[i][0]
            nc = v[1] + d[i][1]
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] <= maps[N-1][N-1]:              #maps를 순회하며 다음 값이 현재값 + 가중치보다 크다면 최소값으로 갱신
                if arr[v[0]][v[1]] < arr[nr][nc]:
                    if maps[nr][nc] > maps[v[0]][v[1]]+arr[nr][nc]-arr[v[0]][v[1]]:
                        maps[nr][nc] = maps[v[0]][v[1]]+arr[nr][nc]-arr[v[0]][v[1]]+1
                        Q.append([nr,nc])
                else:
                    if maps[nr][nc] > maps[v[0]][v[1]]+1:
                        maps[nr][nc] = maps[v[0]][v[1]]+1
                        Q.append([nr, nc])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = [0,0]
    maps = [[10000000000000]*(N) for _ in range(N)]             # maps 를 절대 나올 수 없는 최대값으로 초기화
    bfs(start)
    print(f'#{tc+1} {maps[N-1][N-1]}')