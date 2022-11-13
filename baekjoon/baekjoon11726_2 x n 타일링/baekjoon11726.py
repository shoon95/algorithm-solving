import sys
sys.stdin = open('input.txt')

arr = []
for i in range(0,int(input())+1):
    arr.append(i)

for i in range(3,len(arr)):     # 1, 2번은 기저 조건
    arr[i] = arr[i-2]+arr[i-1]  # 3번 부터 이와 같은 점화식을 통해 값을 구한다.
print(arr[-1]%10007)