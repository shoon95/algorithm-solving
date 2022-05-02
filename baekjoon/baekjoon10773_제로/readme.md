# BAEKJOON 10773 제로

### [🏸문제](https://www.acmicpc.net/problem/10773) 

<hr>



### 💊풀이

> 배열을 미리 생성하고 시간을 최대한 줄이기 위해 sys.stdin.readline을 사용하자

1. sys.stdin.readline을 통해 input을 받아온다.
1. input이 0 이 아니면 pointer를 우측으로 한 칸 이동시키고 해당 포인터 위치에 value를 넣어준다.
1. input이 0이면 pointer를 좌측으로 이동시킨다.
1. pointer 위치까지 모든 value를 더해준 값을 출력한다.

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
j = -1
arr = [[] for _ in range(100000)] # 미리 배열을 생성
for _ in range(N):
    value = int(input())
    if value:
        j += 1                    # 추가되면 pointer를 우측으로 이동시키고 value 추가
        arr[j] = value

    else:
        j -= 1                    # input이 0 이면 pointer를 좌측으로 이동

if j > -1:                        # pointer가 -1 이면 0, 그것보다 크면 포인터 +1 까지 더한 값 출력
    print(sum(arr[:j+1]))
else:
    print(0)
```

<hr>





### 🛀결과

![image-20220430225759954](readme.assets/image-20220430225759954.png)

요즘들으 pointer와 미리 배열을 만들어서 문제를 푸는 것에 아주 맛들리 것 같다... 좋은 건 아닌 것 같은데...

미리 배열을 만들어놓고 해당 배열 내에서 pointer 를 순회하는 방법이 항상 가장 먼저 떠오른다! 이번 pointer 접근 방법은 생각보다 마음에 들었다. 그런데 실제로 정답 제출을 했을 때 4048이라는 무시무시한 시간이 나왔다... (*~~이게 무슨 일이여..)~~* 

하지만! sys.stdin.readline을 쓰니 시간이 증발해버렸다..!!! 

sys.stdin.readline을 자주 자주 애용합시다.

