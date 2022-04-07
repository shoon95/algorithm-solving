import sys
sys.stdin = open('input.txt')

while True:
    n1, n2, n3 = map(int, input().split())
    if n1+n2+n1 == 0:
        break
    if n1**2+n2**2+n3**2 - max(n1, n2, n3)**2==max(n1, n2, n3)**2:      # 주어진 세 수의 제곱의 합에 가장 큰 값의 제곱을 뺀 값이 가장 큰 값의 제곱과 같다면 지각 삼각형
        print('right')
    else:
        print('wrong')