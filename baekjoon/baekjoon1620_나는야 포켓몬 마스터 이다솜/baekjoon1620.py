import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = {}
for i in range(1,N+1):
    arr[(sys.stdin.readline().rstrip())] = i # 포켓몬의 이름을 key 값, 들어오는 순서를 value 로 dictionary에 추가
    i+=1

data = list(arr.keys())                      # dictionary의 key 값들을 리스트로 바꾸어줌

for _ in range(M):
    value = sys.stdin.readline().rstrip()
    if value.isnumeric():                    # input이 숫자면 data에서 해당 idx의 포켓몬 출력
        print(data[int(value)-1])
    else:
        print(arr[value])                    # input이 문자면 dictionary의 해당 key의 value 출력
