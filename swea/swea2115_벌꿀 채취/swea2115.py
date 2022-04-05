import sys
sys.stdin = open('input.txt')

'''
필요한 기능
1. 해당 좌표에서 최대 벌꿀
2. 순회하는 기능
'''

def get_value(idx, M, C):
    visit = [0] * M
    idx_all = []
    for i in range(M):
        idx_all.append([idx[0],idx[1]+i])
    result_end = 0
    for i in range(M, 0,-1):
        def get_combi(n, start, temp,temp2, C):
            nonlocal visit  # 모든 조합의 경우의 수를 구하는 함수
            nonlocal idx_all
            nonlocal result_end
            if len(temp) == n:  # 조합의 개수가 원하는 수가 되는 함수 종료
                if sum(temp) > C:
                    return
                else:
                    if sum(temp2) >= result_end:
                        result_end = sum(temp2)
                    return
            for k in range(start, len(idx_all)):  # start부터 순회하는데 다음 재귀를 호출 할 떄는 현재 i가 순회 시작점이 됨
                if visit[k] == 0:
                    visit[k] = 1
                    get_combi(n, k, temp + [arr[idx_all[k][0]][idx_all[k][1]]],temp2 + [(arr[idx_all[k][0]][idx_all[k][1]])**2], C)
                    visit[k] = 0
        get_combi(i,0,[],[],C)

    return result_end

T = int(input())

for tc in range(T):
    N, M, C = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*(N-M+1) for _ in range(N)]
    dp = [[-1]*(N-M+1) for _ in range(N)]

    result_arr = [[0]*(N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            for m in range(M):
                if j+m < N-M+1:
                    visited[i][j+m] = 1
                if 0 <= j-m:
                    visited[i][j-m] = 1
            if dp[i][j] == -1:
                dp[i][j] = get_value([i,j], M, C)

            dp2 = [[-1] * (N - M + 1) for _ in range(N)]
            for p in range(N):
                for q in range(N-M+1):
                    if visited[p][q] == 1:
                        continue
                    else:
                        if dp[p][q] == -1:
                            dp[p][q] = get_value([p,q], M ,C)
                    dp2[p][q] = dp[p][q]
            result_arr[i][j] = dp[i][j]+max(list(map(lambda n:max(n),dp2)))
    print(f'#{tc+1} {max(list(map(lambda n:max(n),result_arr)))}')



