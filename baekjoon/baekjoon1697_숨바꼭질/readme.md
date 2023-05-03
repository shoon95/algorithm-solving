# BAEKJOON 1967 숨바꼭질

### [🏸문제](https://www.acmicpc.net/problem/1967) 

<hr>



### 💊풀이

> bfs를 통해 가까운 곳 우선으로 탐색

1. bfs를 통해 가까운 곳부터 탐색 시작
2. visited 를 만들어 방문한 곳은 이전 방문한 곳 +1 로 채움

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

def bfs(X, K):
    Q = []
    Q.append(X)
    visited[X] = 1
    while Q:
        X = Q.pop(0)
        for i in (X+1, X-1, 2*X):
            if 0 < i < 100001 and not visited[i]:
                Q.append(i)
                visited[i] = visited[X]+1
            if i == K:
                return visited[X]
visited = [0] * 100001
if N==K:
    print(0)
else:
    print(bfs(N, K))

```

<hr>





### 🛀결과

![스크린샷 2023-05-03 오후 5.33.11.png](./스크린샷 2023-05-03 오후 5.33.11.png)

처음에는 dfs로 접근했다. 그 이유는 dfs로 풀면 재귀로 풀 수 있어 코드가 작성하기 쉬웠기 때문이다.
하지만 dfs로 짤 경우 재귀 초과 또는 메모리 초과 문제가 발생하였다. 그래서 bfs 방식으로 가까운 곳을 우선적으로 탐색했다.
또한 visited를 만들어 중복으로 방문하는 것을 방지하도록 하였다.