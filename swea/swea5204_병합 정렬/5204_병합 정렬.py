import sys
sys.stdin = open('input.txt')
'''
8
69 10 30 2 16 8 31 32
'''
def merge(left, right):
    result = []
    # left, right 둘 중 하나라도 존재
    l_idx = 0
    r_idx = 0
    l_check = len(left)
    r_check = len(right)
    while l_idx < l_check and r_idx < r_check:
        # left, right 모두 존재
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    # left만 존재
    if l_idx < l_check:
        result.extend(left[l_idx:])
    else:
        result.extend(right[r_idx:])

    return result

def merge_sort(a):
    global cnt
    # 기본 파트
    if len(a) == 1:
        return a
    # 유도 파트
    else:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1
        return merge(left, right)

T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)

    print(f'#{tc+1} {arr[N//2]} {cnt}')