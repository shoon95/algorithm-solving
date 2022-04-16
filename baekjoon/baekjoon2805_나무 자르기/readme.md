# BAEKJOON 2805 나무 자르기

### 🏸문제 

https://www.acmicpc.net/problem/2805

<hr>




### 💊풀이

1. 이진 탐색 구현
2. 이진 탐색이 end와 start 위치가 서로 바뀔 때까지 계속해서 진행하고 서로 위치가 바뀌었다면 그때 나무 자르는 높이른 반환하면 된다.

<hr>




### 📌코드

```python
import sys
sys.stdin = open('input.txt')

def get_H(start,end,M):
    global trees

    mid = (end+start)//2                                        # 자르는 높이

    if start > end:                                             # 이진 탐색 종료 조건
        return mid

    h = sum(map(lambda n: n-mid if n-mid > 0 else 0, trees))    # 잘라낸 나무들의 합

    if h >= M:                                                  # 잘라낸 나무들의 합이 목표보다 높으면 자르는 위치를 높임
        start = mid+1
    else:
        end = mid-1                                             # 잘라낸 나무들의 합이 목표보다 작으면 자르는 위치를 낮춤

    return get_H(start,end,M)

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
print(get_H(start,end,M))
```

<hr>




### 🛀결과

![image-20220416235021320](readme.assets/image-20220416235021320.png)

이진 탐색 구현할 수 있어? 라고 묻는 문제이다.

결과적으로 이진 탐색만 구현한다면 쉽게 해결은 가능하다. 다만 정답을 어떤 것을 리턴해야하는지는 약간의 고민이 필요하다. 
