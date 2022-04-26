import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

arr = [0 for _ in range(20001)] # 입력값을 idx하로 하는 배열 생성

N= int(input())

for _ in range(N):              # 입력값이 들어오면 해당 값을 idx로 하여 value에 +1
    arr[int(input())] += 1

for i in range(20001):          # 전체 배열을 순회하면서 value 값만큼 idx를 출력
    for _ in range(arr[i]):
        print(i)