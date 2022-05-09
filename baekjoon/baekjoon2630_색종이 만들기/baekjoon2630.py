import sys
sys. stdin = open('input.txt')

def get_result(arr):                                                        # 분할 정복을 통해 문제 해결
    global white_cnt                                                        # 파란 색종이를 담을 변수
    global blue_cnt                                                         # 하얀 색종이를 담을 변수

    white = 0
    blue = 0
    flag = 0
    length = len(arr)
    for i in range(length):                                                 # 배열을 순회하며 파란색과 하얀색이 모두 있으면 flag를 1로 바꾸고 순회 종료
        for j in range(length):
            if arr[i][j] == 1:
                blue += 1
            else:
                white += 1
            if blue != 0 and white != 0:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:                                                                       # 파란색과 흰색이 모두있으면 배열을 4개의 정사각형으로 나누고 각각 다시 재귀 호출
        get_result(list(map(lambda n:n[0:length//2], arr[0:length//2])))
        get_result(list(map(lambda n: n[0:length // 2], arr[length//2:length])))
        get_result(list(map(lambda n: n[length//2:length], arr[0:length // 2])))
        get_result(list(map(lambda n: n[length//2:length], arr[length//2:length])))
    else:
        if white > 0:                                                                   # 색이 하나만 있다면 각 색을 카운트 해줌
            white_cnt += 1
        else:
            blue_cnt += 1


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

white_cnt = 0                                                                       # 하얀색만 있는 색종이의 수
blue_cnt = 0                                                                        # 파란색만 있는 색종이의 수

get_result(arr)
print(white_cnt)
print(blue_cnt)

