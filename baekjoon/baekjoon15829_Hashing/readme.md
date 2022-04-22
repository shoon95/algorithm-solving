# BAEKJOON 15829 Hashing

### [🏸문제](https://www.acmicpc.net/problem/15829) 

<hr>


### 💊풀이

> 아스키 코드로 변환하여 범위를 확인한다.

1. 주어진 수를 아스키 코드로 변환하여 확인한다.



### 📌코드

```python
import sys
sys.stdin = open('input.txt')
N = int(input())
arr = input()
cnt = 0
for i in range(N):
    cnt += (ord(arr[i])-96) * (31**i)	# 주어진 값을 변환하여 범위 확인
print(cnt%1234567891)
```

<hr>




### 🛀결과
