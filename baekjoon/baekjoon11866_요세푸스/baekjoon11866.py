import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

arr = list(range(1,N+1))
value = K-1                                     # 배열이 1부터 시작하니까 idx 값은 K-1
print('<', end='')

while arr:
    if value >= N:                              # idx 가 배열의 크기 이상이라면 N으로 나눈 나머지
        value = value%N

    if len(arr)==1:                             # 현재 배열의 길이가 1이라면 print를 뒤에 , 없이 출력
        print(arr.pop(value%(N)),end='')
    else:
        print(arr.pop(value % (N)), end=', ')

    value += K-1                                # idx 크기 계속해서 추가
    N -= 1                                      # pop을 해서 배열에서 원소 1개를 제거했으니 길이 N을 1 줄여줌

print('>')



# NEY
# N, K = map(int, input().split())
# idx = K-1
# people = list(range(1, N+1))
# removed = [1] * N
#
# print(f'<{people[idx]}', end='')
# removed[idx] = 0
# idx += 1
# cnt = 0
#
# while 1 in removed:
#     if removed[idx]:
#         cnt += 1
#     if cnt == K:
#         print(f', {people[idx]}', end='')
#         removed[idx] = 0
#         cnt = 0
#     idx = (idx+1)%7
#
# print('>')