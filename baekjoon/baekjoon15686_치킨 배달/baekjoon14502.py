import sys
sys.stdin = open('input.txt')

d = [(-1,0),(1,0),(0,-1),(0,1)]

def get_combi(n, start, temp):              # 모든 조합의 경우의 수를 구하는 함수
    if len(temp) == n:                      # 조합의 개수가 원하는 수가 되는 함수 종료
        combi.append(temp)
        return

    for i in range(start,len(idx)):         # start부터 순회하는데 다음 재귀를 호출 할 떄는 현재 i가 순회 시작점이 됨
        if visit[i] == 0:
            visit[i] = 1
            get_combi(n,i,temp+[idx[i]])
            visit[i] =0

def dfs(r,c):
    for i in range(4):
        nr = r+d[i][0]
        nc = c+d[i][1]
        if 0 <= nr < N and 0<= nc < M and maps[nr][nc] == 0:    #위와 같은 조건이 만족시 maps를 2로 바꾸어주고 계속해서 탐색
            maps[nr][nc]=2
            dfs(nr,nc)



N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

idx = []
combi = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            idx.append([i,j])           # 주어진 배열에서 0인 idx만 뽑아서 해당 idx들의 조합을 계산
visit = [0] * (len(idx)+1)
get_combi(3,0,[])
print(combi)

chickeen = []                           # 바이러스의 위치(idx)를 미리 chickeen 이라는 변수에 할당
for i in range(N):
    if 2 in arr[i]:
        for j in range(M):
            if arr[i][j] ==2:
                chickeen.append([i,j])


mmin = 0
for i in combi:
    maps = [i[:] for i in arr]          # 조합으로 만들어놓은 idx의 0을 1로 바꾸는데 원본은 바꾸지 않기 위해 깊은 복사로 값들을 가져와서 maps에 저장
    cnt = 0

    for j in i:
        maps[j[0]][j[1]] = 1            # 조합으로 만들어놓은 idx들을 가져와 해당 value를 1로 바꾸어줌
    for k in chickeen:                  # 주어진 배열에서 value가 2인 idx에서 dfs 탐색 시작
        dfs(k[0],k[1])
    for m in range(N):                  # dfs탐색이 끝난 후에 0의 개수를 센다
        for n in range(M):
            if maps[m][n] == 0:
                cnt += 1
    if cnt > mmin:                      # 0의 개수가 현재 mmin보다 크면 새로 갱신
        mmin = cnt

print(mmin)