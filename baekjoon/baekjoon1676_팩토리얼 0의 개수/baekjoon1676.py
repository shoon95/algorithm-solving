import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = 1
for i in range(1,N+1):              # N! 계산
    cnt*=i

result = 10
i = 1
while True:
    if cnt % (result ** i) != 0:    # N! 값을 10**i 에서 i를 1부터 1씩 늘려가면서 나눈 나머지가 0이 아닐 때까지 반복
        break
    i += 1

print(i-1)