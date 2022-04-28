import sys
sys.stdin = open('input.txt')

N = int(input())

def check(arr):
    cnt = 0                 # cnt 초기값 0으로 초기화
    for i in arr:           # input이 '(' 라면 cnt += 1
        if i == '(':
            cnt += 1
        else:               # input이 ')' 라면 cnt -= 1
            cnt -= 1
        if cnt < 0:         # cnt가 0보다 작아지면 '(' 보다 ')' 많다는 의미니까 NO
            return('NO')
            break
    if cnt != 0:            # 모든 input을 처리했을 때 cnt != 0 이면 아직 '('가 남았으니까 No
        return('NO')
    else:                   # cnt == 0 이면 모든 괄호가 처리됐음으로 YES
        return('YES')

for _ in range(N):
    arr = list(input())
    print(check(arr))