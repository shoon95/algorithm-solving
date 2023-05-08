# BAEKJOON 11279 최소힙

### [🏸문제](https://www.acmicpc.net/problem/1927) 

<hr>



### 💊풀이

> 최대힙 구현

1. 배열을 만들고 최대힙으로 사용
2. 값을 튜플로 넣어 (우선순위, value)  우선 순위를 통해 값을 추출한다.

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
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-value, value))
```

<hr>





### 🛀결과

![스크린샷 2023-05-08 오전 11.16.41](./스크린샷 2023-05-08 오전 11.16.41.png)

최대힙을 구현하기 위해 기존 value에 음수를 취해서 해당 값으로 우선 순위를 취하도록 했다.s