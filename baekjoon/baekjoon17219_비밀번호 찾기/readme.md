# BAEKJOON 17219 비밀번호 찾기

### [🏸문제](https://www.acmicpc.net/problem/17219) 

<hr>



### 💊풀이

> 딕셔너리를 사용하여 속도를 빠르게 하자

1. input을 띄어쓰기 기준으로 나눈다
1. 앞 부분을 dictionary의 key, 뒷 부분을 dictionary의 value로 사용
1. dictionary의 key를 사용하여 호출

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    key, value = sys.stdin.readline().rstrip().split()  # input을 key 로 dictionary 생성
    dic[key] = value

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])
```

<hr>





### 🛀결과

![image-20220505173831303](readme.assets/image-20220505173831303.png)

*~~이지!~~*
