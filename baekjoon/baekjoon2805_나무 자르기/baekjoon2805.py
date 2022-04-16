import sys
sys.stdin = open('input.txt')

def get_H(start,end,M):
    global trees

    mid = (end+start)//2                                        # 자르는 높이

    if start > end:                                             # 이진 탐색 종료 조건
        return mid

    h = sum(map(lambda n: n-mid if n-mid > 0 else 0, trees))    # 잘라낸 나무들의 합

    if h >= M:                                                  # 잘라낸 나무들의 합이 목표보다 높으면 자르는 위치를 높임
        start = mid+1
    else:
        end = mid-1                                             # 잘라낸 나무들의 합이 목표보다 작으면 자르는 위치를 낮춤

    return get_H(start,end,M)

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
print(get_H(start,end,M))