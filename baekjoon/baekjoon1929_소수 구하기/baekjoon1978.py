import sys
sys.stdin = open('input.txt')

N = int(input())

def check_1(value):
    if value == 1:                  # input이 1이면 소수가 아님
        return 0
    else:
        for i in range(2,value):    # input이 2 이상일 때는 자기보다 작은 수로 나누어지는지 확인
            if value%i == 0:
                return 0
    return 1


cnt = 0
for i in map(int,input().split()):
    cnt += check_1(i)
print(cnt)