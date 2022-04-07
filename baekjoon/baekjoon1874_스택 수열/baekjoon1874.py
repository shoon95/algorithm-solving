import sys
sys.stdin = open('input.txt')
N = int(input())

lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0                         # 숫자가 몇까지 들어갔는지 기록
result = []                     # 연산자를 담을 리스트
stack =[]                       # 실제 수를 담을 리스트
flag =1                         # 만약 수열을 완성할 수 없으면 flag를 -1로 바꾸어줌
for i in lst:
    if flag==-1:                # 수열을 완성할 수 없으면 반복 종료
        break
    if i > cnt:                 # 주어진 리스트의 값이 cnt 보다 크면
        while i != cnt:         # 리스트의 값과 cnt 가 같을 때까지 push 해주면서 cnt를 +1 해줌
            cnt+=1
            result +=['+']
            stack.append(cnt)
        stack.pop()             # cnt와 리스트의 값이 같으면 stack에서 pop해줌
        result+=['-']
    elif i < cnt:               # 만약 cnt보다 현재 리스트의 값이 작다면
        while True:             # stack의 pop 값이 리스트의 값과 같을 때가지 계속해서 pop
            result+=['-']
            if len(stack)==0:   # stack 의 크기가 0인데 아직도 리스트의 값과 같은게 나오지 않았다면
                flag = -1       # 수열을 완성할 수 없음으로 flag를 -1로 바꾸고 함수 종료
                break
            if stack.pop() == i:
                break
if flag == 1:
    for i in result:
        print(i)
else:
    print('NO')