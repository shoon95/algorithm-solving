# BAEKJOON 10845 ํ

### [๐ธ๋ฌธ์ ](https://www.acmicpc.net/problem/10845) 

<hr>



### ๐ํ์ด

> input์ sys.stdin.readline์ ํตํด ๋ฐ์์ผ ์๊ฐ ์ด๊ณผ๋ฅผ ํผํ  ์ ์๋ค

1. sys.stdin.readline์ ํตํด input์ ๋ฐ์์จ๋ค.
1. ๋ฌธ์ ์์ ์ฃผ์ด์ง ๋ช๋ น์ด๊ฐ input์ ์กด์ฌํ๋์ง ํ์ธ
1. ํด๋น input์ ๋ฐ๋ฅธ ๊ฒฐ๊ณผ ๊ฐ์ ์ถ๋ ฅ
1. Q ๋ฅผ ๊ตฌํํ๋ฉด ๋๋ค.

<hr>

### ๐์ฝ๋

```python
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

rear = front = -1
Q = []
for _ in range(N):
    data = input()
    if 'push' in data:
        rear += 1
        Q.append(data.split()[1])
    elif 'front' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[front+1])
    elif 'back' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[rear])
    elif 'size' in data:
        print(rear-front)
    elif 'pop' in data:
        if front == rear:
            print(-1)
        else:
            print(Q[front+1])
            front += 1
    elif 'empty' in data:
        if front == rear:
            print(1)
        else:
            print(0)
```

<hr>





### ๐๊ฒฐ๊ณผ

![image-20220427223355478](readme.assets/image-20220427223355478.png)

Q๋ฅผ ๊ตฌํํ๋ ๋ฌธ์ ์ด๋ค. Q๋ฅผ class๋ฅผ ์จ์๋ ๊ตฌํ ๊ฐ๋ฅํ๋ฐ ๋์ค์๋ class๋ฅผ ์ฌ์ฉํด์ ๊ตฌํํ๋ ๊ฒ๋ ๋ค์ ์ฐ์ตํด๋ด์ผ ๊ฒ ๋ค. ์๊ฐ ์ด๊ณผ๋ฅผ ํผํ๊ธฐ ์ํด sys.stdin.readline์ ์จ์ค์ผ ๋๋ค๋ ์ฌ์ค์ ์์ง ๋ง์!
