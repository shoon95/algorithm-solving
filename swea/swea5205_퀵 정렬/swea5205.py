import sys
sys.stdin = open('input.txt')

# 로무토 파티션 방식 -> 가장 간단(속도는 살짝 더 느림)
# 로무토 파티션 방식이란 항상 맨 오른쪽의 피벗을 택하는 방식

# 로무토 파티션 함수
def partition(lo, hi, A):
    pivot = A[hi]                                     # idx hi 의 value가 pivot이 됨
    left = lo                                         # 주어진 lo를 left로 설정
    for right in range(lo, hi):                       # right를 lo, hi까지 순회
        if A[right] < pivot:                          # right의 값이 pivot 보다 작다면 left와 right의 value를 바꾸어주고 left와 right를 모두 한 칸씩 증가
            A[left], A[right] = A[right], A[left]     # right의 값이 pivot 보다 크다면 right의 값만 증가
            left+=1
    A[left], A[hi] = A[hi], A[left]                   # right의 값이 끝까지 순회햇다면 left와의 value와와 prvot을 서로 바꾸어줌
    return left

# 메인 함수
def quick_sort(lo, hi, A):
    if lo < hi:
        pivot = partition(lo, hi,A)                   # 계산을 위해 임의의 수 하나 pivot 설정
        quick_sort(lo, pivot-1, A)                    # 피벗 기준 왼쪽을 재귀 호출 해줌
        quick_sort(pivot+1, hi, A)                    # 피벗 기준 오른쪽을 재귀 호출 해줌

T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, len(A)-1, A)
    print(f'#{tc+1} {A[len(A)//2]}')

