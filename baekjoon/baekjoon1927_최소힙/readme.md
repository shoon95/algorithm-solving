# BAEKJOON 1927 최소힙

### [🏸문제](https://www.acmicpc.net/problem/1927) 

<hr>



### 💊풀이

> 최소힙 구현

1. 배열을 만들고 최소힙으로 사용
2. 조건에 따라 input에 맞추어 처리

<hr>

### 📌코드

```python
import sys
import heapq
sys.stdin = open('input.txt')

heap = []

N = int(input())
for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0 and len(heap) == 0:
        print(0)
    elif value == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, value)
```

<hr>





### 🛀결과

![스크린샷 2023-05-08 오전 11.09.06](./스크린샷 2023-05-08 오전 11.09.06.png)

최소힙 문제이다. 최소힙을 알고 있다면 너무너무 쉽게 풀 수 있다.

직접 최소힙을 class로 구현해보려고 했지만 시간이 너무 오래걸렸고 조건 처리를 정확히 하지 못했다. 따라서 내가 최소힙이 어떤 구조로 작동하는지 정확히 알고 있는 상태라고 판단해서 간단하게 라이브러리를 사용하여 구현했다