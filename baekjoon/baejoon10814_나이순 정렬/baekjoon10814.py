import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(201)]

for _ in range(N):
    age, name = input().split()
    arr[int(age)].append(name)  # 나이를 idx로 하고 해당 idx에 이름을 추가

for i in range(201):
    if len(arr[i]) > 0:         # 값이 들어있는 배열만 idx만 순회하면서 나이와 이름 출력
        for j in arr[i]:
            print(f'{i} {j}')