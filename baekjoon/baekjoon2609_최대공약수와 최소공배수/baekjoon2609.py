import sys
sys.stdin = open('input.txt')

Q = [list(map(int,input().split()))]    # input을 list형태로 받는다

temp = []                               # 나눌 수 있는 수를 저장할 빈 list 초기화
while Q:
    n, m = Q.pop()                      # 처음에 받은 list에서 값을 꺼내서 n,m에 담아주기
    for i in range(2,min(m,n)+1):       # 주어진 값 중 작은 숫자를 마지막 범위로 해서 2부터 순회
        if n%i==0 and m%i==0:           # n,m 둘 다 나눌 수 있는 수가 나타나면
            temp.append(i)              # 나눌 수 있는 수의 모임 temp에 저장 후
            Q.append([n//i,m//i])       # 나눴을 때 몫을 list에 새로 담아주고 순회 종료
            break                       # Q 가 빌 때까지 계속해서 반복
cnt_1 = 1                               # cnt_1 변수를 1로 초기화
for i in temp:                          # 나눌 수 있는 수들의 곱 : 최대 공약수
    cnt_1*=i
print(cnt_1)
print(cnt_1*n*m)                        # 최대 공약수 * 마지막 n,m의 몫 : 최소 공배수수

