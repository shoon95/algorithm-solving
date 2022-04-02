import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1):
    arr = list(map(int, input().split()))

    N =arr[0]                               # N: 정류장 수
    stop = arr[1:]                          # 충전지 용량

    dp = [N]*N                              # 정류장 수만큼 dp 생성, 각 요소는 나올 수 없는 큰 수인 N으로 초기화 0 < M < N
    dp[N-1] = 0                             # 기저 조건인 맨 마지막 값을 0으로 초기화
    for i in range(len(stop), -1, -1):      # 뒤에서부터 순회하면서 도착지에 도착할 수 있는 최소값으로 업데이트
        for j in range(i-1, -1,-1):
            print(f'i:{i} - j:{j}')
            print(f'stop : {stop}')
            print(f'dp : {dp}\n')
            if i <= j+stop[j]:              # j에서 i까지 올 수 있다면
                dp[j] = min(dp[i]+1, dp[j]) # dp[i]와, dp[j] 값을 비교해서 더 작은 값으로 초기화화
    print(f'#{tc+1} {dp[0]-1}')