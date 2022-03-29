import sys
sys.stdin = open('input.txt')

T = int(input())
d = [(0,1),(1,0)]

def dfs(row, col, cnt, last_row, last_col):
    global min
    if cnt > min:
        return

    if row == last_row and col == last_col:
        if cnt < min:
            min = cnt
    else:
        for i in range(2):
            if 0 <= row + d[i][0] < N and 0 <= col + d[i][1] < N:
                dfs(row + d[i][0],col + d[i][1],cnt+arr[row + d[i][0]][col + d[i][1]], last_row, last_col)


for tc in range(T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    last_row = last_col = N-1

    min = (N+N-1)*10
    dfs(0,0,arr[0][0],last_row,last_col)
    print(f'#{tc+1} {min}')