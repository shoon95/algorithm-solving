import sys
sys.stdin = open('input.txt')

arr = [[0] * 15 for _ in range(15)]
arr[0] = list(range(1,16))

for i in range(15):                             # 배열의 0 열을 전부 1로 초기화
    arr[i][0] =1

for i in range(1, 15):                          # 1,1 부터 순회하며 앞 열과 윗 행을 더한 값을 본인의 값으로 채워줌
    for j in range(1,15):
        arr[i][j] = arr[i-1][j]+arr[i][j-1]

T = int(input())


for tc in range(T):
    N = int(input())
    M = int(input())
    print(arr[N][M-1])
