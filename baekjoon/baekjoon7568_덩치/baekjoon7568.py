import sys
sys.stdin = open('input.txt')

N = int(input())

arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = []
for i in arr:
    k = 1                               # 초기값 1 설정
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]: # 나보다 큰 값 존재할 때마다 1씩 더 추가
            k+=1
    result.append(k)
print(*result)