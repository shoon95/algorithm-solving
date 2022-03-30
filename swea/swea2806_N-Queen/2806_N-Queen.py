import sys
sys.stdin = open('input.txt')

d = [(-1,-1), (-1,1)]

def recur(row, col_list,cross):
    global cnt

    if len(col_list) == N :                                 # col_list에 담긴 요소의 개수가 N과 같다면 cnt르 1추가하고 종료
        cnt += 1
        return

    if row >= N:                                            # 행을 N 만큼 순회했다면 종료
        return

    for i in range(N):                                      # 열을 주어진 N만큼 순회
        if i not in col_list and (row,i) not in cross:      # i가 아직 방문하지 않은 열이고 방문하지 않은 대각이면 진행
            cross_check = 0                                 # 행의 수만큼만 앞의 대각에 퀸이 존재하는 확인
            for j in range(1, row+1):
                if (row+j*d[0][0],i+j*d[0][1]) in cross or (row+j*d[1][0],i+j*d[1][1]) in cross:
                    cross_check +=1                         # 앞의 대각에 퀸이 존재하면 cross_check를 1로 바꾸고 순회를 종료
                    break
            if cross_check ==0:                             # 앞의 대각에 퀸이 존재하지 않앗다면 다음 재귀를 호출
                recur(row+1, col_list+[i],cross+[(row,i)])



T = int(input())

for tc in range(T):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    cnt = 0
    recur(0, [],[])
    print(f'#{tc+1} {cnt}')