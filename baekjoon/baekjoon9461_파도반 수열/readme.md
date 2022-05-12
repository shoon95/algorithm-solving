# BAEKJOON 9461 파도반 수열

### [🏸문제](https://www.acmicpc.net/problem/9461) 

<hr>



### 💊풀이

> 점화식을 구하고 dp를 사용하자!

1. input: N의 크기만큼 dp 배열 생성
1. 배열의 기저 조건 [0:3]을 모두 1로 초기화
1. 현재 idx의 값은 (idx - 3)의 value + (idx - 2)의 value

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0]*N
    arr[0:3] = [1,1,1]              # dp 배열 기저 조건 초기화

    for i in range(3,N):
        arr[i] = arr[i-3]+arr[i-2]  # 현재 idx의 값은 idx-3의 값 + idx-2
    print(arr[-1])                  # 순회 종료 후 제일 마지막 값 출력

```

<hr>





### 🛀결과

![image-20220512195615767](readme.assets/image-20220512195615767.png)

문제가 그냥 dp를 사용해서 풀어라! 라고 대놓고 주어진 수준이다. 그래서 더 무서웠다... 하지만 문제를 읽고 예시를 보니 점화식을 찾기가 생각보다 엄청 쉬웠다. 앞에 풀었던 dp 문제들이 훨씬 어려웠다.

dp 문제와 재귀 문제들은 항상 풀고나면 희열감이 느껴져서 좋지만 풀기 전에는 무섭고 풀 때는 어렵다...😂
