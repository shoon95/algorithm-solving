import sys
import heapq
sys.stdin = open('input.txt')

heap = []

N = int(input())
for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0 and len(heap) == 0:
        print(0)
    elif value == 0:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-value, value))