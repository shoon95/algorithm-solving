import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def partition(lo, hi, arr):
    pivot = arr[hi]
    left = lo
    for right in range(lo, hi):
        if arr[right] < pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
    arr[left], arr[hi] = arr[hi], arr[left]
    return left

def quick_sort(lo, hi , arr):
    if lo < hi:
        pivot = partition(lo, hi, arr)
        quick_sort(lo, pivot-1, arr)
        quick_sort(pivot+1,hi,arr)

N= int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

quick_sort(0, len(arr)-1,arr)
for i in arr:
    print(i)