# BAEKJOON 9375 패션왕 신해빈

### [🏸문제](https://www.acmicpc.net/problem/9375) 

<hr>



### 💊풀이

> 0개 또는 1개를 뽑는 경우의 수를 구하자

1. 주어진 input을 띄어쓰기를 기준으로 value와 key로 나눈다.
1. 미리 만들어 놓은 dictionary의 key 에 input에서 받은 key가 존재하지 않으면 dictionary 에 key 추가하고 value 넣어준다.
1. key가 이미 존재하면 해당 key에 value를 append 해준다.
1. 각 key의 value 길이 +1 을 한 값이 0개 또는 1개를 뽑는 경우의 수
1. 모든 경우의 수를 더하고 모든 옷의 종류가 0개씩 뽑는 경우의 수를 제거하기 위해 cnt -=1 후 출력

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

def get_result(dic):
    global cnt

    for i in dic:                   	# 각각 종류에서 1개 또는 0개를 고르는 경우의 수
        cnt *= len(dic[i])+1
    print(cnt-1)                    	# 모든 종류의 옷을 0개씩 고른 경우를 제외

T = int(input())

for tc in range(T):

    N = int(input())

    dic = {}
    cnt = 1
    for _ in range(N):                  # 주어진 input 중 옷의 종류가 dictionary에 없으면 key에 추가, 있으면 해당 키에 value 추가
        value, idx = input().split()
        if idx in dic:
            dic[idx] += [value]
        else:
            dic[idx] = [value]
    get_result(dic)
```

<hr>





### 🛀결과

![image-20220511224651320](readme.assets/image-20220511224651320.png)

처음에는 딕셔너리 각각의 value 길이를 for 문으로 중첩해서 돌면서 cnt += 1 해주고 마지막 cnt -= 1 을 해주려고 했다. 하지만 아무리 생각해보아도 key의 갯수가 정해지지 않은 상태에서 for 문을 key의 갯수에 맞춰서 자동으로 중첩해서 생성되게 하는 방법을 찾지 못했다. 그래서 그러면 for 문을 중첩하며 count 할 때 어떤 규칙이 있을까르 고민하다가 각 key의 길이에 +1씩 더해줘서 곱해주면 이것이 for문 중첩과 동일하다는 것을 생각했다.*~~(너무 당연한 얘기..ㅜ)~~*
