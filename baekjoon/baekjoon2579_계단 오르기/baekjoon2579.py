import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

if N != 1:                                                      # N이 1이면 바로 input 출력
    dp = [0] *(N+1)
    dp[1] = arr[0]                                              # 기저조건 0:3 초기화
    dp[2] = arr[0]+arr[1]

    for i in range(3, len(arr)+1):                              # 3번 째 앞에까지 최대값에 2번 앞의 값 더한 값과 2번째 앞까지 최댓값 중 큰 값에 현재 값을 더해준다.
        dp[i] = max(dp[i-3]+arr[i-2], dp[i-2]) + arr[i-1]
    print(dp[-1])
else:
    print(arr[-1])