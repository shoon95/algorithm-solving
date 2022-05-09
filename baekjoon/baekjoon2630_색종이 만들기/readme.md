# BAEKJOON 2630 색종이 만들기

### [🏸문제](https://www.acmicpc.net/problem/2630) 

<hr>



### 💊풀이

> 분할 정복을 통해 문제를 해결하자

1. 주어진 배열에 1과 0 모두 존재하는지 확인
1. 1과 -이 둘 다 존재한다면 배열의 4분할 하여 각각 다시 재귀 함수 호출 (분할 정복)
1. 배열에 1과 0이 중 하나만 존재한다면 존재하는 색의 종이 수 +=1

<hr>

### 📌코드

```python
import sys
sys. stdin = open('input.txt')

def get_result(arr):                                                        # 분할 정복을 통해 문제 해결
    global white_cnt                                                        # 파란 색종이를 담을 변수
    global blue_cnt                                                         # 하얀 색종이를 담을 변수

    white = 0
    blue = 0
    flag = 0
    length = len(arr)
    for i in range(length):                                                 # 배열을 순회하며 파란색과 하얀색이 모두 있으면 flag를 1로 바꾸고 순회 종료
        for j in range(length):
            if arr[i][j] == 1:
                blue += 1
            else:
                white += 1
            if blue != 0 and white != 0:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:                                                                       # 파란색과 흰색이 모두있으면 배열을 4개의 정사각형으로 나누고 각각 다시 재귀 호출
        get_result(list(map(lambda n:n[0:length//2], arr[0:length//2])))
        get_result(list(map(lambda n: n[0:length // 2], arr[length//2:length])))
        get_result(list(map(lambda n: n[length//2:length], arr[0:length // 2])))
        get_result(list(map(lambda n: n[length//2:length], arr[length//2:length])))
    else:
        if white > 0:                                                                   # 색이 하나만 있다면 각 색을 카운트 해줌
            white_cnt += 1
        else:
            blue_cnt += 1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

white_cnt = 0                                                                       # 하얀색만 있는 색종이의 수
blue_cnt = 0                                                                        # 파란색만 있는 색종이의 수

get_result(arr)
print(white_cnt)
print(blue_cnt)
```

<hr>





### 🛀결과

![image-20220509205223386](readme.assets/image-20220509205223386.png)

분할 정복 문제를 오랜만에 만났다. 문제를 딱 보자마자 분할 정복으로 해결해야 된다는 감이 왔다. 방향을 잡고나니 쉽게 해결 할 수 있었다. 다만 배열을 4개로 나누어 줄 때 list(map(lambda))를 사용했는데 예전에 lambda를 사용 후 list로 묶어주면 속도가 급격히 떨어진다고 지인이 알려준 적이 있었다. 때문에 해당 방법 말고 다른 방법으로 구현할까 고민했지만 숫자의 크기가 그리 크지 않았기 때문에 그냥 사용해서 구현했다.

오랜만에 재귀로 문제를 푸니까 재밌었다. *~~(항상 잘 풀리면 재밌지 ㅎ)~~*
