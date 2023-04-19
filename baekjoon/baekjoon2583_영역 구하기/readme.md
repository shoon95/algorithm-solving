# BAEKJOON 2583  영역 구하기

### [🏸문제](https://www.acmicpc.net/problem/2583) 

<hr>



### 💊풀이

> 네모가 아닌 영역을 돌면서 끊기기 전까지 체크

1. 주어진 배열을 색이 칠해진 영역에 특정 값을 넣어서 불러온다.
1. 배열을 순회하며 현재 인덱스가 칠해진 영역이 아닐 때만 cnt를 올리고 해당 cnt를 딕셔너리의 키 값으로 넣어준다.
1. 해당 영역부터 bfs 순회를 시작하여 끊기기 전까지 계속 순회하고 이때 순회하는 영역을 cnt 값으로 동일하게 넣어주며 dictionary[cnt]+=1 한다.

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

d = [(-1,0),(1,0), (0, -1), (0, 1)]

M, N, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            maps[y][x] = 9999

check = {}

def bfs(start_row, start_col, cnt):
    queue = []
    maps[start_row][start_col] = cnt 
    queue.append([start_row, start_col])
    check[cnt] = 1
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r+d[i][0]
            nc = c+d[i][1]
            if 0 <= nr < M and 0 <= nc  < N and maps[nr][nc] == 0:
                maps[nr][nc] = cnt
                queue.append([nr, nc])
                check[cnt] += 1
cnt = 1
for r in range(M):
    for c in range(N):
        if maps[r][c] == 0:
            bfs(r, c, cnt)
            cnt += 1

result = [i[1] for i in sorted(list(check.items()), key=lambda n:n[1])]
print(len(result))
for i in result:
    print(i, end=' ')
```

<hr>





### 🛀결과

![스크린샷 2023-04-19 오전 9.42.46](./스크린샷 2023-04-19 오전 9.42.46.png)

Bfs 를 통해 문제를 해결했다. 반복문이 너무 많은 것 같고, 전체 배열을 반복해서 순회하는 느낌이 강해 비효율적이며 시간 복잡도에서 문제가 생기지 않을까 했는데 다행이도 통과했다.(느리지 않게!)

오랜만에 알고리즘을 풀어서 input을 받을 때와 bfs 순회법을 떠올리며 코드를 짜는게 힘들었다. 다시 1일 1알고를 하며 익숙해지도록 하자!
