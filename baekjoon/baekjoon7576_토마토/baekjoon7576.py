import sys
sys.stdin = open('input.txt')

d=[(1,0),(-1,0),(0,1),(0,-1)]                                                           # 하,상,우,좌 네 방향 순회를 위한 배열 생성

def get_start(M,N):                                                                     # 토마토의 위치를 알아내기 위해 배열에서 1을 찾는 함수
    for i in range(M):
        for j in range(N):
            if arr[i][j]==1:
                start.append([i,j])
    return start

def bfs(start):                                                                         # 처음 토마토들의 위치를 시작 지점으로 넣고 bfs 순회 시작
    Q = []
    Q.extend(start)
    rear = len(start)-1
    front = -1
    while front != rear:                                                                # Q에서 더이상 꺼낼 항목이 없으면 종료
        front += 1
        r, c = Q[front]
        for i in range(4):                                                              # 4방향 순회
            nr = r+d[i][0]
            nc = c+d[i][1]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc]==0 and visited[nr][nc]==0:   # 아직 방문하지 않고 토마토가 없는 곳
                visited[nr][nc] = visited[r][c] + 1                                     # 이전 visitd+1 을 해줘서 날짜를 세어줌
                Q.append([nr,nc])                                                       # 이후 다음 이동할 인덱스를 Q에 넣어주기
                rear+=1                                                                 # rear +1

def get_result():                                                                       # 결과를 출력하는 함수
    max = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0 :                                                     # 0 이 있다면 토마토가 전부 열리지는 못했음으로 -1 출력
                return -1
            else:                                                                       # 0이 없다면 max를 계속 갱신해줌
                if visited[i][j] > max:
                    max = visited[i][j]
    return max-1

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

visited= [item[:] for item in arr]                                                      # 2차원 배열 깊은 복사
start = []

start=get_start(M,N)
for i in start:
    visited[i[0]][i[1]] =1

bfs(start)

print(get_result())

