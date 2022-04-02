N = int(input())
#상향식
def fib(n):
    if n==0:                        # 초기값 0, 1 설정
        return 0
    if n==1:
        return 1
    for i in range(2, n+1):         # bottom-up 방식으로 2부터 n까지 순차적으로 dp를 채워감, 이떄 해당 값은 기존에 계산 해놓은 값을 이용하여 계산
        dp[i] = dp[i-1]+dp[i-2]
    return dp[i]

#하향식
def fib(n):                         # top-down 방식
    if n==0:                        # 초기값 0, 1 설정
        return 0
    if n==1:
        return 1
    if dp[n]!=0:                    # dp에 n 값이 존재한다면 해당 값 return
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)     # dp에 n 값이 존재하지 않는다면 재귀 함수를 호출해서 해당 결과를 dp에 담아줌
    return dp[n]                    # 위에 담긴 dp 값을 통해 다음 재귀는 dp[n] 을 return함으로 한 번 했던 재귀 호출은 다시 하지 않음

dp =[0] * 301
dp[0] = 0
dp[1] = 1

print(fib(N))