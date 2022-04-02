# BAEKJOON 2748 피보나치 수2

### 문제 

https://www.acmicpc.net/problem/2748

<hr>


### 풀이

피보나치 수열은 재귀 호출을 통해 풀 수 있는 대표적인 예제이다. 하지만 원하는 값이 클 경우 재귀는 매우 비효율적이다. 따라서 기존에 계산한 값을 다시 사용하여 시간을 엄청나게 단축시키는 dp를 사용하면 매우 효율적으로 풀 수 있다.

해당 문제는 dp를 top-down 방식과 bottom-up 방식 두 가지로 풀어보았다.

먼저 dp에 초기값을 설정해준 후 n번 째 숫자까지 순차적으로 채워가는 방식은 bottom-up이며,

dp에 초기값을 설정해준 후 재귀호출을 통해 기존 값이 memorization에 존재한다면 해당 값을 사용하여 더이상 재귀 호출을 하지 않는 방식은 top-down 방식이다.

<hr>


### 코드

```python
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
```

<hr>


### 결과

![화면 캡처 2022-03-30 202506](readme.assets/화면 캡처 2022-03-30 202506.png)

해당 문제를 dp를 통해 해결한다는 사실을 알고 있었기에 쉽게 풀 수 있었다. 기본적인 dp의 형태를 이해하고 다른 형태에서 dp를 적용하여 풀 수 있도록 노력하자.