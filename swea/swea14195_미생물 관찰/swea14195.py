import sys
sys.stdin = open('input.txt')


def dfs(start):
    global temp
    global visited
    global cnt
    visited[start[0]][start[1]] = 1
    cnt += 1
    if cnt > temp:
        temp = cnt

    for i in range(4):
        nr = start[0] + d[i][0]
        nc = start[1] + d[i][1]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] != 1 and arr[start[0]][start[1]] == arr[nr][nc]: # 기존과 같을 때만 dfs를 순회

            dfs([nr,nc])

d = [(-1,0),(1,0),(0,-1),(0,1)]

T = int(input())



for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(list(input())) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]
    A = [0]
    B = [0]
    for i in range(N):
        for j in range(M):
            temp = 0
            if arr[i][j] == 'A' and visited[i][j] != 1: # A일 때는 dfs 순회 후 A 배열에 추가
                cnt = 0
                dfs([i,j])
                A.append(temp)
            elif arr[i][j] == 'B' and visited[i][j] != 1:   # B일 때는 dfs 순회 후 B 배열에 추가
                cnt = 0
                dfs([i, j])
                B.append(temp)
            elif arr[i][j] =='_':
                visited[i][j] = 1

    print(f'#{tc+1} {len(A)-1} {len(B)-1} {max(max(A),max(B))}')    # 길이와 최댓값을 구해서 출력