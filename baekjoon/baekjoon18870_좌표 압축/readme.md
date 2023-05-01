# BAEKJOON 18870 좌표 압축

### [🏸문제](https://www.acmicpc.net/problem/18870) 

<hr>



### 💊풀이

> 중복 제거 후 정렬한다음 인덱스를 활용

1. 인풋을 받아와 중복을 제거하고 정렬
1. 정렬된 수의 idx를 value, 값을 key로 하는 딕셔너리 생성

<hr>

### 📌코드

```python
N = int(input())
numbers = list(map(int, input().split()))

nums = sorted(list(set(numbers)))
dic = {}
for cnt, i in enumerate(nums):
    dic[i] = cnt

for i in numbers:
    print(dic[i])
```

<hr>





### 🛀결과

![스크린샷 2023-05-01 오후 8.19.46](./스크린샷 2023-05-01 오후 8.19.46.png)

처음에 카운팅 정렬을에서 아이디어를 얻어 카운팅 배열을 통해 풀어보려고 했다. 하지만 조건에서 수의 범위가 너무 커서 카운팅 배열을 만들 경우 메모리 초과가 날 수 있다는 사실을 알았다. 그럼에도 복습 겸 도전해보았는데 역시나 에러가 발생했다. 때문에 숫자의 중복을 없애고 정렬 시킨 후 해당 수의 idx를 value로 수의 값을 key로 딕셔너리를 만들어 풀었다.

정확한 시간 복잡도를 고려하고 풀지는 않았지만 수가 최대 백만개여서 충분히 가능할 거라고 생각했다.
