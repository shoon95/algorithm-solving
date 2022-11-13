import sys
sys.stdin = open('input.txt')

def solution_1(name): # 파이써닉
    order = [name[i] > name[i + 1] for i in range(0, N - 1)]    # 문자열 간의 대소 비교를 통해 1번과 2번, 2번과 3번 ~ 을 끝까지 반복
    if sum(order) == N - 1: # 대소 비교한 값을 다 더했을 때 1이라면 내림차순 정렬되어있다는 것
        print('DECREASING')
    elif sum(order) == 0:   # 대소 비교한 값을 다 더했을 때 0이라면 오름차순 정렬 되어있다느 ㄴ것
        print('INCREASING')
    else:                   # 이 외에 중간 중간 0과 1이 섞여있다면 정렬되지 않은 것
        print('NEITHER')

N = int(input())
name = [input() for _ in range(N)]

# print(name)
# print(name[3] > name[4])
# print([list(map(lambda n:ord(n), i)) for i in name])


