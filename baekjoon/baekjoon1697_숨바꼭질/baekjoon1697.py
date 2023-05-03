import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

def bfs(X, K):
    Q = []
    Q.append(X)
    visited[X] = 1
    while Q:
        X = Q.pop(0)
        for i in (X+1, X-1, 2*X):
            if 0 < i < 100001 and not visited[i]:
                Q.append(i)
                visited[i] = visited[X]+1
            if i == K:
                return visited[X]
visited = [0] * 100001
if N==K:
    print(0)
else:
    print(bfs(N, K))
