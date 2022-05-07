import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [9999999] * (N+1)

if N==1:                                                # dp 기저 조건 초기화
    dp[0:2] = [0,0]
elif N==2:
    dp[0:3] = [0,0,1]
else:
    dp[0:4] = [0, 0, 1,1]

for i in range(3,len(dp)):                              # 기저 조건 이후부터 dp 순회
    if i % 2 == 0 and i % 3 ==0:                        # 이전 값의 +1과 나눈 몫을 idx로 하는 값 중 최소값을 비교
        dp[i] = min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3]+1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[-1])