N = int(input())
dp = [9999] *(N+1)                  # 나올 수 없는 큰 수로 dp 초기화
cnt3=1                              # 3의 배수의 idx에 초기값 설정
cnt5=1                              # 5의 배수의 idx에 초기값 설정
for i in range(1,N+1):
    if i%3 ==0:                     # 3의 배수 idx에 값 넣어주기
        dp[i]=cnt3
        cnt3+=1
    if i%5 ==0:                     # 5의 배수 idx에 값 넣어주기
        dp[i] = cnt5
        cnt5+=1

for i in range(3, N+1):             # 3뒤 부터 5칸 앞에에 1더한 것과 본인 중 더 작은 값으로 업데이트
    dp[i] = min(dp[i-5]+1,dp[i])

if dp[-1]==9999:
    print(-1)
else:
    print(dp[-1])
