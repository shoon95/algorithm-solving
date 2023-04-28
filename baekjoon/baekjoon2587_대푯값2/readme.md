# BAEKJOON 2587 대푯값2

### [🏸문제](https://www.acmicpc.net/problem/17626) 

<hr>



### 💊풀이

> 주어진 인풋을 받아와서 정렬 시키자

1. 인풋을 받아와 빈 리스트에 추가
1. 리스트에서 평균값과 중앙값을 출력

<hr>

### 📌코드

```python
import sys
sys.stdin = open('input.txt')

numbers = []
for i in range(5):
    numbers.append(int(input()))

print(sum(numbers)//5)
print(sorted(numbers)[2])

```

<hr>





### 🛀결과

![스크린샷 2023-04-28 오후 5.36.09](./스크린샷 2023-04-28 오후 5.36.09.png)

So EEEEEEEEEEEEEEEasy
