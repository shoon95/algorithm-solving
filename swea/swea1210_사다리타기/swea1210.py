import sys
sys.stdin = open('input.txt')

# 0:좌, 1:우, 2:상
d = [(-1,0),(1,0),(0,-1)]

def find_two(arr)->tuple:
    num = 0
    for idx in arr[-1][:]:
        if idx == 2:
            return (99, num)
        num += 1

def get_start_point(r,c)->int:
    for i in range(3):
        nr = r+d[i][1]  # 위로 올라가기
        nc = c+d[i][0]  # 좌, 우 탐색
        if 0 <= nr <= 99 and 0 <= nc <= 99 and arr[nr][nc] == 1:    # 탐색 범위 조건
            if nr == 0 and arr[nr][nc] == 1:
                print( f'#{tc} {nc}')   # 사다리의 시작점을 찾으면 재귀 정답 출력
            arr[nr][nc] = 0 # 이미 지나온 길은 0으로 바꾸어 다시 못지나가게
            return get_start_point(nr, nc) # return 으로 재귀를 호출해서 조건을 만족하는 값 하나를 찾으면 다른 재귀는 호출하지 않고 전부 종료

for _ in range(10):
    tc = int(input()) # tc 받기
    arr = [list(map(int, input().split())) for _ in range(100)] # 사다리를 표시하는 2차원 배열 받기
    end_point = find_two(arr)   # 사다리가 끝나는 지점인 2의 위치 찾기
    get_start_point(end_point[0], end_point[1]) # 2에서 시작 지점으로 찾아서 올라가기